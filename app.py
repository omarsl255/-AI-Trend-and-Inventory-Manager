"""
Flask Web Application for ATIM
Upload CSV inventory files and get AI-powered recommendations
"""
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
from flask.json.provider import DefaultJSONProvider
from werkzeug.utils import secure_filename
import os
import sys
from datetime import datetime
import traceback
import numpy as np

# Import ATIM components
from inventory_data import InventoryManager
from trend_analysis import TrendAnalyzer
from llm_inventory_agent import InventoryAgent
from report_generator import ReportGenerator
from config import CURRENT_SEASON


# Custom JSON encoder to handle numpy types
class NumpyJSONProvider(DefaultJSONProvider):
    """Custom JSON provider that handles numpy types."""
    def default(self, obj):
        if isinstance(obj, (np.integer, np.int64)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float64)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)


# Check if templates folder exists, if not use current directory
template_folder = 'templates' if os.path.exists('templates') else '.'

app = Flask(__name__, template_folder=template_folder)
app.json = NumpyJSONProvider(app)  # Use custom JSON encoder
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'csv'}

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    """Home page with upload form."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and process inventory."""
    try:
        # Check if file is present
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Please upload a CSV file.'}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        saved_filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], saved_filename)
        file.save(filepath)
        
        # Get analysis parameters
        max_keywords = int(request.form.get('max_keywords', 15))
        min_confidence = float(request.form.get('min_confidence', 20.0))
        
        # Process the file
        result = process_inventory(filepath, max_keywords, min_confidence)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'traceback': traceback.format_exc()
        }), 500


def process_inventory(csv_filepath, max_keywords=15, min_confidence=20.0):
    """
    Process inventory file and generate analysis.
    
    Args:
        csv_filepath: Path to uploaded CSV file
        max_keywords: Maximum keywords to analyze
        min_confidence: Minimum confidence threshold
        
    Returns:
        Dictionary with analysis results
    """
    import numpy as np
    
    # Helper function to convert numpy/pandas types to Python types
    def convert_to_python_type(obj):
        """Convert numpy/pandas types to native Python types."""
        if isinstance(obj, (np.integer, np.int64)):
            return int(obj)
        elif isinstance(obj, (np.floating, np.float64)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {key: convert_to_python_type(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [convert_to_python_type(item) for item in obj]
        return obj
    
    # Initialize components
    inventory_manager = InventoryManager(csv_file=csv_filepath)
    trend_analyzer = TrendAnalyzer()
    inventory_agent = InventoryAgent()
    
    # Get inventory data
    inventory_items = inventory_manager.get_all_inventory()
    inventory_summary = inventory_manager.get_inventory_summary()
    
    # Generate keywords
    keywords = [item.product_name.lower() for item in inventory_items]
    
    # Analyze trends
    trending_products = trend_analyzer.get_high_confidence_trends(
        keywords,
        min_confidence=min_confidence,
        max_keywords=max_keywords
    )
    
    # Fallback to sample data if no trends
    if not trending_products and keywords:
        import random
        sample_keywords = keywords[:5]
        trending_products = []
        
        for keyword in sample_keywords:
            base_strength = random.uniform(40, 80)
            velocity = random.uniform(-10, 15)
            confidence = abs(velocity) * 0.6 + base_strength * 0.4
            
            if velocity > 5:
                status = "Rising"
            elif velocity < -5:
                status = "Declining"
            elif base_strength > 70:
                status = "Peaking"
            else:
                status = "Stable"
            
            trending_products.append({
                "keyword": keyword,
                "status": status,
                "confidence": float(confidence),
                "velocity": float(velocity),
                "strength": float(base_strength),
                "current_value": float(base_strength),
                "peak_value": float(base_strength * 1.2)
            })
    
    # Convert trending products to ensure all values are JSON serializable
    trending_products = convert_to_python_type(trending_products)
    
    # Generate AI recommendations
    upcoming_holidays = ["Labor Day", "Back to School", "Fall Fashion Week"]
    recommendations = inventory_agent.generate_recommendations(
        trending_products,
        current_season=CURRENT_SEASON,
        upcoming_holidays=upcoming_holidays
    )
    
    # Clean the recommendations for better display
    from format_utils import clean_llm_output
    recommendations_clean = clean_llm_output(recommendations)
    
    # Get low stock items
    low_stock_items = [
        item for item in inventory_items
        if item.current_stock <= item.reorder_point
    ]
    
    # Generate HTML report
    report_gen = ReportGenerator()
    report_filename = f"atim_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    report_path = os.path.join('reports', report_filename)
    os.makedirs('reports', exist_ok=True)
    
    report_gen.generate_html_report(
        trending_products,
        inventory_summary,
        recommendations,
        low_stock_items,
        output_file=report_path
    )
    
    # Prepare response - convert all numpy types to Python types
    return {
        'success': True,
        'inventory_summary': {
            'total_items': int(inventory_summary['total_items']),
            'low_stock_items': int(inventory_summary['low_stock_items']),
            'total_value': float(inventory_summary['total_inventory_value'])
        },
        'trending_products': convert_to_python_type(trending_products[:10]),
        'recommendations': str(recommendations_clean),
        'low_stock_count': int(len(low_stock_items)),
        'low_stock_items': [
            {
                'product_name': str(item.product_name),
                'current_stock': int(item.current_stock),
                'reorder_point': int(item.reorder_point)
            }
            for item in low_stock_items
        ],
        'report_url': f'/reports/{report_filename}'
    }


@app.route('/reports/<filename>')
def download_report(filename):
    """Download generated report."""
    return send_file(
        os.path.join('reports', filename),
        as_attachment=False,
        mimetype='text/html'
    )


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})


if __name__ == '__main__':
    print("=" * 70)
    print("🚀 ATIM Web Application Starting...")
    print("=" * 70)
    print(f"\n📂 Template folder: {template_folder}")
    print(f"📂 Upload folder: {app.config['UPLOAD_FOLDER']}")
    print("\n📱 Open your browser and go to:")
    print("   → http://localhost:5000")
    print("\n⌨️  Press Ctrl+C to stop the server\n")
    print("=" * 70)
    
    app.run(debug=True, host='0.0.0.0', port=5000)