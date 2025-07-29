import streamlit as st
import pandas as pd
import json
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Data Science UI Mockup Tool",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling and force light mode
st.markdown("""
<style>
    /* Force light mode regardless of system settings */
    .stApp {
        background-color: #ffffff !important;
        color: #262730 !important;
    }
    
    /* Sidebar light mode */
    .css-1d391kg, .css-1q8dd3e {
        background-color: #f8f9fa !important;
        color: #262730 !important;
    }
    
    /* Main content area light mode */
    .main .block-container {
        background-color: #ffffff !important;
        color: #262730 !important;
    }
    
    /* Headers and text */
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4 !important;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2c3e50 !important;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
        margin: 1.5rem 0 1rem 0;
    }
    .info-box {
        background-color: #f8f9fa !important;
        border-left: 4px solid #17a2b8;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0.25rem;
        color: #262730 !important;
    }
    .metric-container {
        background-color: #ffffff !important;
        border: 1px solid #dee2e6;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 0.5rem 0;
        color: #262730 !important;
    }
    
    /* Force light mode for all text elements */
    .stMarkdown, .stText, p, h1, h2, h3, h4, h5, h6, span, div {
        color: #262730 !important;
    }
    
    /* Force light mode for inputs and widgets */
    .stSelectbox > div > div, .stTextInput > div > div, .stDataFrame {
        background-color: #ffffff !important;
        color: #262730 !important;
    }
    
    /* Ensure metric components are light */
    [data-testid="metric-container"] {
        background-color: #ffffff !important;
        border: 1px solid #dee2e6 !important;
        color: #262730 !important;
    }
    
    /* Force light mode for tables and dataframes */
    .dataframe {
        background-color: #ffffff !important;
        color: #262730 !important;
    }
    
    /* Code blocks light mode */
    .stCodeBlock {
        background-color: #f8f9fa !important;
        color: #262730 !important;
    }
</style>
""", unsafe_allow_html=True)

def load_data():
    """Load grocery store data from CSV files"""
    data_path = Path("data")
    
    if not data_path.exists():
        st.error("Data directory not found. Please run data generation first.")
        return None, None, None, None
    
    try:
        departments = pd.read_csv(data_path / "departments.csv")
        categories = pd.read_csv(data_path / "categories.csv")
        subcategories = pd.read_csv(data_path / "subcategories.csv")
        products = pd.read_csv(data_path / "products.csv")
        return departments, categories, subcategories, products
    except FileNotFoundError as e:
        st.error(f"Data file not found: {e}")
        return None, None, None, None

def show_documentation():
    """Display the documentation page"""
    st.markdown('<h1 class="main-header">📖 Documentation & Architecture</h1>', unsafe_allow_html=True)
    
    # Architecture Overview
    st.markdown('<h2 class="section-header">🏗️ System Architecture</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    <strong>🎯 Purpose:</strong> This application serves as a UI mockup tool for data science teams to quickly prototype 
    and test user interfaces with realistic hierarchical data structures.
    </div>
    """, unsafe_allow_html=True)
    
    # Create architecture diagram
    st.markdown("### System Components")
    
    architecture_mermaid = """
    graph TB
        A[User Interface<br/>Streamlit App] --> B[Data Layer<br/>CSV Files]
        A --> C[Documentation<br/>Architecture & Guides]
        A --> D[Interactive Explorer<br/>Data Visualization]
        
        B --> E[departments.csv<br/>Level 1: Store Departments]
        B --> F[categories.csv<br/>Level 2: Product Categories]
        B --> G[subcategories.csv<br/>Level 3: Product Subcategories]
        B --> H[products.csv<br/>Level 4: Individual Products]
        
        D --> I[Filtering & Search]
        D --> J[Hierarchical Navigation]
        D --> K[Data Statistics]
        
        style A fill:#e1f5fe
        style B fill:#f3e5f5
        style C fill:#e8f5e8
        style D fill:#fff3e0
    """
    
    st.markdown("#### High-Level Architecture")
    from streamlit.components.v1 import html
    
    # Use a simpler approach to show the diagram
    st.code(architecture_mermaid, language="mermaid")
    
    st.markdown("""
    **Key Components:**
    - **User Interface Layer**: Streamlit-based web interface for easy interaction
    - **Data Layer**: Flat CSV files storing hierarchical grocery store data
    - **Documentation**: This page with architecture and usage guides
    - **Interactive Explorer**: Tools for browsing and filtering the mock data
    """)
    
    # Data Structure
    st.markdown('<h2 class="section-header">📊 Data Structure</h2>', unsafe_allow_html=True)
    
    data_structure_mermaid = """
    graph TD
        A[Departments<br/>Level 1] --> B[Categories<br/>Level 2]
        B --> C[Subcategories<br/>Level 3]
        C --> D[Products<br/>Level 4]
        
        A1[Fresh Foods] --> B1[Fruits]
        A1 --> B2[Vegetables]
        A1 --> B3[Meat & Seafood]
        
        A2[Packaged Goods] --> B4[Snacks]
        A2 --> B5[Beverages]
        A2 --> B6[Pantry Items]
        
        B1 --> C1[Citrus Fruits]
        B1 --> C2[Berries]
        B1 --> C3[Tropical Fruits]
        
        C1 --> D1[Oranges - Navel]
        C1 --> D2[Lemons - Meyer]
        C1 --> D3[Limes - Key]
        
        style A fill:#ffcdd2
        style B fill:#f8bbd9
        style C fill:#e1bee7
        style D fill:#c5cae9
    """
    
    st.code(data_structure_mermaid, language="mermaid")
    
    st.markdown("""
    **4-Level Hierarchy:**
    1. **Departments** (8 departments): Major store sections like Fresh Foods, Packaged Goods
    2. **Categories** (24 categories): Product groupings like Fruits, Vegetables, Dairy
    3. **Subcategories** (72 subcategories): Specific product types like Citrus Fruits, Leafy Greens
    4. **Products** (500+ products): Individual items with details like pricing and inventory
    """)
    
    # File Structure
    st.markdown('<h2 class="section-header">📁 File Structure</h2>', unsafe_allow_html=True)
    
    st.code("""
📁 Streamlit App
├── 📄 app.py                  # Main application file
├── 📄 requirements.txt        # Python dependencies
├── 📄 README.md              # Setup and usage instructions
├── 📁 data/                  # Data storage directory
│   ├── 📄 departments.csv    # Level 1: Store departments
│   ├── 📄 categories.csv     # Level 2: Product categories  
│   ├── 📄 subcategories.csv  # Level 3: Product subcategories
│   └── 📄 products.csv       # Level 4: Individual products
└── 📁 scripts/              # Utility scripts
    └── 📄 generate_data.py   # Data generation script
    """, language="text")
    
    # Usage Guide
    st.markdown('<h2 class="section-header">🚀 Usage Guide</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    **Getting Started:**
    1. **Installation**: Run `pip install -r requirements.txt`
    2. **Data Generation**: Execute `python scripts/generate_data.py` to create sample data
    3. **Run App**: Launch with `streamlit run app.py`
    4. **Explore**: Use the sidebar navigation to switch between Documentation and Data Explorer
    
    **For Non-Technical Users:**
    - The app provides an intuitive web interface - no coding required
    - Use the Data Explorer to browse and filter grocery store items
    - All data is stored in simple CSV files that can be opened in Excel
    - Modify data files directly to test different scenarios
    """)
    
    # Technical Details
    st.markdown('<h2 class="section-header">⚙️ Technical Implementation</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Technologies Used:**
        - **Streamlit**: Web application framework
        - **Pandas**: Data manipulation and analysis
        - **Python**: Core programming language
        - **CSV**: Simple flat file storage
        """)
    
    with col2:
        st.markdown("""
        **Key Features:**
        - **Zero Database**: All data in flat CSV files
        - **Hierarchical Navigation**: Drill-down capabilities
        - **Real-time Filtering**: Dynamic data exploration
        - **Responsive Design**: Works on desktop and mobile
        """)

def show_data_explorer():
    """Display the data exploration page"""
    st.markdown('<h1 class="main-header">🛒 Grocery Store Data Explorer</h1>', unsafe_allow_html=True)
    
    # Load data
    departments, categories, subcategories, products = load_data()
    
    if departments is None:
        st.warning("Please generate sample data first by running `python scripts/generate_data.py`")
        return
    
    # Data overview metrics
    st.markdown('<h2 class="section-header">📊 Data Overview</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("Departments", len(departments))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("Categories", len(categories))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("Subcategories", len(subcategories))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-container">', unsafe_allow_html=True)
        st.metric("Products", len(products))
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Hierarchical filters
    st.markdown('<h2 class="section-header">🔍 Interactive Filters</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        selected_dept = st.selectbox(
            "Select Department",
            ["All"] + departments['name'].tolist(),
            key="dept_filter"
        )
    
    # Filter categories based on department
    if selected_dept != "All":
        dept_id = departments[departments['name'] == selected_dept]['id'].iloc[0]
        filtered_categories = categories[categories['department_id'] == dept_id]
    else:
        filtered_categories = categories
    
    with col2:
        selected_cat = st.selectbox(
            "Select Category",
            ["All"] + filtered_categories['name'].tolist(),
            key="cat_filter"
        )
    
    # Filter subcategories based on category
    if selected_cat != "All":
        cat_id = filtered_categories[filtered_categories['name'] == selected_cat]['id'].iloc[0]
        filtered_subcategories = subcategories[subcategories['category_id'] == cat_id]
    else:
        filtered_subcategories = subcategories
    
    with col3:
        selected_subcat = st.selectbox(
            "Select Subcategory",
            ["All"] + filtered_subcategories['name'].tolist(),
            key="subcat_filter"
        )
    
    # Filter products based on selections
    filtered_products = products.copy()
    
    if selected_subcat != "All":
        subcat_id = filtered_subcategories[filtered_subcategories['name'] == selected_subcat]['id'].iloc[0]
        filtered_products = filtered_products[filtered_products['subcategory_id'] == subcat_id]
    elif selected_cat != "All":
        subcat_ids = filtered_subcategories['id'].tolist()
        filtered_products = filtered_products[filtered_products['subcategory_id'].isin(subcat_ids)]
    elif selected_dept != "All":
        cat_ids = filtered_categories['id'].tolist()
        subcat_ids = subcategories[subcategories['category_id'].isin(cat_ids)]['id'].tolist()
        filtered_products = filtered_products[filtered_products['subcategory_id'].isin(subcat_ids)]
    
    # Display filtered products
    st.markdown('<h2 class="section-header">🛍️ Products</h2>', unsafe_allow_html=True)
    
    if len(filtered_products) > 0:
        # Search functionality
        search_term = st.text_input("🔍 Search products", placeholder="Enter product name...")
        
        if search_term:
            filtered_products = filtered_products[
                filtered_products['name'].str.contains(search_term, case=False, na=False)
            ]
        
        # Sort options
        sort_by = st.selectbox("Sort by", ["name", "price", "stock_quantity"])
        sort_order = st.radio("Order", ["Ascending", "Descending"], horizontal=True)
        
        ascending = sort_order == "Ascending"
        filtered_products = filtered_products.sort_values(sort_by, ascending=ascending)
        
        # Display products in a nice format
        st.dataframe(
            filtered_products[['name', 'price', 'stock_quantity', 'unit']],
            use_container_width=True,
            hide_index=True
        )
        
        st.info(f"Showing {len(filtered_products)} products")
    else:
        st.warning("No products found with the current filters.")

def show_hierarchy_visualization():
    """Display hierarchy visualization with Sankey diagram"""
    st.markdown('<h1 class="main-header">🌐 Hierarchy Visualization</h1>', unsafe_allow_html=True)
    
    # Load data
    departments, categories, subcategories, products = load_data()
    
    if departments is None:
        st.warning("Please generate sample data first by running `python scripts/generate_data.py`")
        return
    
    # Controls for the diagram
    show_products = st.checkbox("Include Products Layer", value=False, help="Warning: May slow performance with 1000+ products")
    
    # Create Sankey diagram
    if show_products:
        fig = create_full_sankey_diagram(departments, categories, subcategories, products)
        st.info("💡 Showing all 4 levels. **Width = product count, Color = quality** (🟢 Good, ⚪ Neutral, 🔴 Poor)")
    else:
        fig = create_sankey_diagram(departments, categories, subcategories)
        st.info("💡 Showing 3 levels. **Width = product count, Color = quality** (🟢 Good, ⚪ Neutral, 🔴 Poor)")
    
    # Display the diagram
    st.plotly_chart(fig, use_container_width=True)

def get_quality_color(products_df):
    """Calculate the dominant quality color for a group of products"""
    if len(products_df) == 0:
        return "rgba(158, 158, 158, 0.4)"  # Default gray
    
    # Count quality distribution
    quality_counts = products_df['quality'].value_counts()
    total_products = len(products_df)
    
    # Calculate percentages
    good_pct = quality_counts.get('good', 0) / total_products
    poor_pct = quality_counts.get('poor', 0) / total_products
    
    # Color based on dominant quality (with thresholds)
    if good_pct >= 0.6:  # 60%+ good = green
        return "rgba(76, 175, 80, 0.4)"    # Green
    elif poor_pct >= 0.3:  # 30%+ poor = red  
        return "rgba(244, 67, 54, 0.4)"    # Red
    else:  # Mixed or neutral dominant = gray
        return "rgba(158, 158, 158, 0.4)"  # Gray

def create_sankey_diagram(departments, categories, subcategories):
    """Create a 3-level Sankey diagram (Departments → Categories → Subcategories)"""
    
    # Load products data for counting
    _, _, _, products = load_data()
    
    # Define neutral color palette
    dept_color = "rgba(149, 165, 166, 0.8)"  # Light gray
    cat_color = "rgba(127, 140, 141, 0.8)"   # Medium gray  
    subcat_color = "rgba(52, 73, 94, 0.8)"   # Dark gray
    
    # Create nodes
    nodes = []
    node_colors = []
    
    # Add department nodes
    for _, dept in departments.iterrows():
        nodes.append(dept['name'])
        node_colors.append(dept_color)
    
    # Add category nodes  
    for _, cat in categories.iterrows():
        nodes.append(cat['name'])
        node_colors.append(cat_color)
    
    # Add subcategory nodes
    for _, subcat in subcategories.iterrows():
        nodes.append(subcat['name'])
        node_colors.append(subcat_color)
    
    # Create links
    source = []
    target = []
    value = []
    link_colors = []
    
    # Departments to Categories (width = product count, color = quality)
    for _, cat in categories.iterrows():
        dept_idx = departments[departments['id'] == cat['department_id']].index[0]
        cat_idx = len(departments) + categories[categories['id'] == cat['id']].index[0]
        
        # Count products and calculate quality in this category
        cat_subcats = subcategories[subcategories['category_id'] == cat['id']]
        cat_products = products[products['subcategory_id'].isin(cat_subcats['id'])]
        product_count = len(cat_products)
        
        # Calculate dominant quality for this category
        color = get_quality_color(cat_products)
        
        source.append(dept_idx)
        target.append(cat_idx)
        value.append(max(1, product_count))  # Use product count as width
        link_colors.append(color)
    
    # Categories to Subcategories (width = product count, color = quality)
    for _, subcat in subcategories.iterrows():
        cat_idx = len(departments) + categories[categories['id'] == subcat['category_id']].index[0]
        subcat_idx = len(departments) + len(categories) + subcategories[subcategories['id'] == subcat['id']].index[0]
        
        # Count products and calculate quality in this subcategory
        subcat_products = products[products['subcategory_id'] == subcat['id']]
        product_count = len(subcat_products)
        
        # Calculate dominant quality for this subcategory
        color = get_quality_color(subcat_products)
        
        source.append(cat_idx)
        target.append(subcat_idx)
        value.append(max(1, product_count))  # Use product count as width
        link_colors.append(color)
    
    # Create the Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="rgba(0,0,0,0.5)", width=0.5),
            label=nodes,
            color=node_colors
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=link_colors
        )
    )])
    
    fig.update_layout(
        title="Grocery Store Hierarchy Flow (Width = Product Count, Color = Quality)",
        title_x=0.5,
        font_size=12,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=600
    )
    
    return fig

def create_full_sankey_diagram(departments, categories, subcategories, products):
    """Create a 4-level Sankey diagram (includes products - may be slow)"""
    
    # Limit products for performance
    max_products_per_subcat = 5
    limited_products = []
    
    for _, subcat in subcategories.iterrows():
        subcat_products = products[products['subcategory_id'] == subcat['id']].head(max_products_per_subcat)
        limited_products.append(subcat_products)
    
    limited_products_df = pd.concat(limited_products, ignore_index=True)
    
    # Create the diagram with limited products
    return create_sankey_diagram_with_products(departments, categories, subcategories, limited_products_df)

def create_sankey_diagram_with_products(departments, categories, subcategories, products):
    """Helper function to create Sankey with products layer"""
    
    # Define colors
    colors = [
        "rgba(149, 165, 166, 0.8)",  # Departments - light gray
        "rgba(127, 140, 141, 0.8)",  # Categories - medium gray
        "rgba(52, 73, 94, 0.8)",     # Subcategories - dark gray
        "rgba(44, 62, 80, 0.8)"      # Products - darker gray
    ]
    
    # Create nodes
    nodes = []
    node_colors = []
    
    # Add all levels
    for _, dept in departments.iterrows():
        nodes.append(f"🏪 {dept['name']}")
        node_colors.append(colors[0])
    
    for _, cat in categories.iterrows():
        nodes.append(f"📦 {cat['name']}")
        node_colors.append(colors[1])
    
    for _, subcat in subcategories.iterrows():
        nodes.append(f"🔖 {subcat['name']}")
        node_colors.append(colors[2])
    
    for _, product in products.iterrows():
        nodes.append(f"🛍️ {product['name'][:20]}...")  # Truncate long names
        node_colors.append(colors[3])
    
    # Create links with proper indexing
    source = []
    target = []
    value = []
    link_colors = []
    
    dept_offset = 0
    cat_offset = len(departments)
    subcat_offset = len(departments) + len(categories)
    product_offset = len(departments) + len(categories) + len(subcategories)
    
    # Get all products for counting (use original products, not limited)
    all_products = load_data()[3]  # Get full product list
    
    # Departments to Categories (width = product count, color = quality)
    for _, cat in categories.iterrows():
        dept_idx = departments[departments['id'] == cat['department_id']].index[0]
        cat_idx = cat_offset + categories[categories['id'] == cat['id']].index[0]
        
        # Count products and calculate quality in this category
        cat_subcats = subcategories[subcategories['category_id'] == cat['id']]
        cat_products = all_products[all_products['subcategory_id'].isin(cat_subcats['id'])]
        product_count = len(cat_products)
        
        # Calculate dominant quality for this category
        color = get_quality_color(cat_products)
        
        source.append(dept_idx)
        target.append(cat_idx)
        value.append(max(1, product_count))
        link_colors.append(color)
    
    # Categories to Subcategories (width = product count, color = quality)
    for _, subcat in subcategories.iterrows():
        cat_idx = cat_offset + categories[categories['id'] == subcat['category_id']].index[0]
        subcat_idx = subcat_offset + subcategories[subcategories['id'] == subcat['id']].index[0]
        
        # Count products and calculate quality in this subcategory
        subcat_products = all_products[all_products['subcategory_id'] == subcat['id']]
        product_count = len(subcat_products)
        
        # Calculate dominant quality for this subcategory
        color = get_quality_color(subcat_products)
        
        source.append(cat_idx)
        target.append(subcat_idx)
        value.append(max(1, product_count))
        link_colors.append(color)
    
    # Subcategories to Products (color = individual product quality)
    for _, product in products.iterrows():
        subcat_idx = subcat_offset + subcategories[subcategories['id'] == product['subcategory_id']].index[0]
        product_idx = product_offset + products[products['id'] == product['id']].index[0]
        
        # Color based on individual product quality
        quality_color = {
            'good': "rgba(76, 175, 80, 0.4)",    # Green
            'neutral': "rgba(158, 158, 158, 0.4)", # Gray  
            'poor': "rgba(244, 67, 54, 0.4)"      # Red
        }.get(product['quality'], "rgba(158, 158, 158, 0.4)")
        
        source.append(subcat_idx)
        target.append(product_idx)
        value.append(1)  # Each individual product has weight 1
        link_colors.append(quality_color)
    
    # Create the diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=10,
            thickness=15,
            line=dict(color="rgba(0,0,0,0.5)", width=0.5),
            label=nodes,
            color=node_colors
        ),
        link=dict(
            source=source,
            target=target,
            value=value,
            color=link_colors
        )
    )])
    
    fig.update_layout(
        title="Complete Grocery Store Hierarchy (Width = Product Count, Color = Quality)",
        title_x=0.5,
        font_size=10,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=800
    )
    
    return fig

def main():
    """Main application function"""
    
    # Initialize page state
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Documentation'
    
    # Simple sidebar navigation with buttons
    with st.sidebar:
        # Display logo with no hover and crisp rendering
        st.markdown("""
        <style>
            [data-testid="stSidebar"] [data-testid="stImage"] > img {
                cursor: default !important;
                pointer-events: none !important;
                image-rendering: -webkit-optimize-contrast !important;
                image-rendering: crisp-edges !important;
            }
            [data-testid="stSidebar"] [data-testid="stImage"]:hover {
                transform: none !important;
            }
        </style>
        """, unsafe_allow_html=True)
        
        st.image("xi-logo.png", use_container_width=True)
        st.markdown("---")
        
        # Navigation buttons
        if st.button("📖 Documentation", use_container_width=True, 
                     type="primary" if st.session_state.current_page == 'Documentation' else "secondary"):
            st.session_state.current_page = 'Documentation'
            st.rerun()
            
        if st.button("🔍 Data Explorer", use_container_width=True,
                     type="primary" if st.session_state.current_page == 'Data Explorer' else "secondary"):
            st.session_state.current_page = 'Data Explorer'
            st.rerun()
            
        if st.button("🌐 Hierarchy Visualization", use_container_width=True,
                     type="primary" if st.session_state.current_page == 'Hierarchy' else "secondary"):
            st.session_state.current_page = 'Hierarchy'
            st.rerun()
    
    # Route to appropriate page
    if st.session_state.current_page == "Documentation":
        show_documentation()
    elif st.session_state.current_page == "Data Explorer":
        show_data_explorer()
    elif st.session_state.current_page == "Hierarchy":
        show_hierarchy_visualization()

if __name__ == "__main__":
    main() 