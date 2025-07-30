import streamlit as st
import pandas as pd
import json
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
from streamlit_tree_select import tree_select

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
        return None, None, None, None, None
    
    try:
        departments = pd.read_csv(data_path / "departments.csv")
        categories = pd.read_csv(data_path / "categories.csv")
        subcategories = pd.read_csv(data_path / "subcategories.csv")
        products = pd.read_csv(data_path / "products.csv")
        temporal_quality = pd.read_csv(data_path / "temporal_quality.csv")
        return departments, categories, subcategories, products, temporal_quality
    except FileNotFoundError as e:
        st.error(f"Data file not found: {e}")
        return None, None, None, None, None

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
    departments, categories, subcategories, products, _ = load_data()
    
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

def create_quality_waterfall_chart(selected_product_ids, temporal_quality):
    """Create a waterfall chart showing quality distribution changes over time"""
    if not selected_product_ids:
        return None
    
    # Filter temporal data for selected products
    filtered_temporal = temporal_quality[temporal_quality['product_id'].isin(selected_product_ids)]
    
    if filtered_temporal.empty:
        return None
    
    # Calculate quality distribution for each time period
    period_quality_counts = (
        filtered_temporal.groupby(['period_index', 'period_name', 'quality'])
        .size()
        .unstack(fill_value=0)
        .reset_index()
        .sort_values('period_index')  # Sort by chronological order
    )
    
    # Calculate cumulative changes from the baseline
    baseline_good = period_quality_counts.iloc[0]['good'] if 'good' in period_quality_counts.columns else 0
    baseline_neutral = period_quality_counts.iloc[0]['neutral'] if 'neutral' in period_quality_counts.columns else 0
    baseline_poor = period_quality_counts.iloc[0]['poor'] if 'poor' in period_quality_counts.columns else 0
    
    # Prepare waterfall data
    periods = period_quality_counts['period_name'].tolist()
    good_changes = []
    neutral_changes = []
    poor_changes = []
    
    for i, row in period_quality_counts.iterrows():
        if i == 0:  # First period is baseline
            good_changes.append(row.get('good', 0))
            neutral_changes.append(row.get('neutral', 0))
            poor_changes.append(row.get('poor', 0))
        else:
            prev_row = period_quality_counts.iloc[i-1]
            good_changes.append(row.get('good', 0) - prev_row.get('good', 0))
            neutral_changes.append(row.get('neutral', 0) - prev_row.get('neutral', 0))
            poor_changes.append(row.get('poor', 0) - prev_row.get('poor', 0))
    
    # Create the waterfall chart
    fig = go.Figure()
    
    # Add traces for each quality level
    fig.add_trace(go.Waterfall(
        name="Good Quality",
        orientation="v",
        measure=["absolute"] + ["relative"] * (len(periods) - 1),
        x=periods,
        textposition="outside",
        text=[f"+{val}" if val > 0 else str(val) for val in good_changes],
        y=good_changes,
        connector={"line": {"color": "rgb(63, 63, 63)"}},
        increasing={"marker": {"color": "#2E8B57"}},
        decreasing={"marker": {"color": "#DC143C"}},
        totals={"marker": {"color": "#4682B4"}}
    ))
    
    fig.update_layout(
        title="Quality Distribution Changes Over Time",
        title_x=0.5,
        showlegend=False,
        xaxis_title="Time Period",
        yaxis_title="Quality Count Change",
        font_size=12,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    
    return fig

def create_quality_distribution_chart(selected_product_ids, temporal_quality):
    """Create a stacked bar chart showing quality distribution over time"""
    if not selected_product_ids:
        return None
    
    # Filter temporal data for selected products
    filtered_temporal = temporal_quality[temporal_quality['product_id'].isin(selected_product_ids)]
    
    if filtered_temporal.empty:
        return None
    
    # Calculate quality distribution for each time period
    period_quality_counts = (
        filtered_temporal.groupby(['period_index', 'period_name', 'quality'])
        .size()
        .unstack(fill_value=0)
        .reset_index()
        .sort_values('period_index')  # Sort by chronological order
    )
    
    # Create stacked bar chart
    fig = go.Figure()
    
    colors = {
        'good': '#7CB9A8',      # Soft Seafoam Green
        'neutral': '#9B9B9B',   # Soft Grey
        'poor': '#D4827E'       # Soft Coral
    }
    
    for quality in ['good', 'neutral', 'poor']:
        if quality in period_quality_counts.columns:
            fig.add_trace(go.Bar(
                name=quality.title(),
                x=period_quality_counts['period_name'],
                y=period_quality_counts[quality],
                marker_color=colors[quality],
                text=period_quality_counts[quality],
                textposition='inside'
            ))
    
    fig.update_layout(
        title="Quality Distribution Over Time (Selected Products)",
        title_x=0.5,
        barmode='stack',
        xaxis_title="Time Period",
        yaxis_title="Number of Products",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        font_size=12,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400
    )
    
    return fig

def get_status_indicator(status):
    """Get emoji indicator for product status"""
    status_indicators = {
        'approved': '📦',
        'recommended': '🔍',
        'rejected': '❌'
    }
    return status_indicators.get(status, '📦')

def filter_products_by_status(products, show_recommended=True, show_rejected=False, show_approved=True):
    """Filter products based on status preferences"""
    filtered = products.copy()
    
    if not show_recommended:
        filtered = filtered[filtered['status'] != 'recommended']
    if not show_rejected:
        filtered = filtered[filtered['status'] != 'rejected']
    if not show_approved:
        filtered = filtered[filtered['status'] != 'approved']
    
    return filtered

def create_count_label(name, total_products, recommended_products):
    """Create enhanced label showing total products and recommendations"""
    if recommended_products > 0:
        return f"{name} ({total_products} products, {recommended_products} recommendations)"
    else:
        return f"{name} ({total_products} products)"

def show_tree_hierarchy():
    """Display interactive tree hierarchy with streamlit-tree-select"""
    st.markdown('<h1 class="main-header">🌳 Interactive Tree Hierarchy</h1>', unsafe_allow_html=True)
    
    # Load data
    departments, categories, subcategories, products, temporal_quality = load_data()
    
    if departments is None:
        st.warning("Please generate sample data first by running `python scripts/generate_data.py`")
        return
    
    # Product Status Filtering - Add to sidebar
    with st.sidebar:
        if st.session_state.current_page == 'Tree Hierarchy':
            st.markdown("---")
            st.markdown("### 🎛️ Product Filters")
            
            # Status filter controls
            show_recommended = st.checkbox("🔍 Show Recommended Products", value=True, key="show_recommended")
            show_approved = st.checkbox("📦 Show Approved Products", value=True, key="show_approved")
            show_rejected = st.checkbox("❌ Show Rejected Products", value=False, key="show_rejected")
            
            # Summary of current filters
            status_summary = []
            if show_recommended: status_summary.append("Recommended")
            if show_approved: status_summary.append("Approved") 
            if show_rejected: status_summary.append("Rejected")
            
            if status_summary:
                st.info(f"Showing: {', '.join(status_summary)}")
            else:
                st.warning("No products will be visible with current filters!")
    
    # Filter products based on sidebar controls
    filtered_products = filter_products_by_status(
        products, 
        show_recommended=show_recommended,
        show_rejected=show_rejected, 
        show_approved=show_approved
    )
    
    # Show filtering stats
    total_products = len(products)
    filtered_count = len(filtered_products)
    recommended_count = len(products[products['status'] == 'recommended'])
    
    st.markdown('<h2 class="section-header">🔍 Tree-Based Navigation</h2>', unsafe_allow_html=True)
    
    # Display filter statistics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Products", total_products)
    with col2:
        st.metric("Showing", filtered_count)
    with col3:
        st.metric("Recommended", recommended_count)
    with col4:
        approval_rate = f"{(total_products - recommended_count) / total_products * 100:.1f}%" if total_products > 0 else "0%"
        st.metric("Approval Rate", approval_rate)
    
    st.markdown("""
    <div class="info-box">
    <strong>🎯 Interactive Tree Selection:</strong> This view allows you to select at ALL hierarchy levels! 
    Choose entire departments (🏢), specific categories (📂), subcategories (🏷️), or even individual products (🛒) using the checkbox tree below. 
    The system will intelligently aggregate all your selections - perfect for granular product analysis!
    <br><br>
    <strong>📋 Status Indicators:</strong> 
    🔍 = Recommended (pending approval) | 
    📦 = Approved (live products) | 
    ❌ = Rejected (removed from consideration)
    </div>
    """, unsafe_allow_html=True)
    
    # Build tree structure for streamlit-tree-select
    def build_tree_nodes():
        tree_nodes = []
        
        for _, dept in departments.iterrows():
            # Get categories for this department
            dept_categories = categories[categories['department_id'] == dept['id']]
            
            # Count total and recommended products in this department (filtered)
            dept_subcats = subcategories[subcategories['category_id'].isin(dept_categories['id'])]
            dept_products = filtered_products[filtered_products['subcategory_id'].isin(dept_subcats['id'])]
            dept_count = len(dept_products)
            dept_recommended_count = len(dept_products[dept_products['status'] == 'recommended'])
            
            dept_node = {
                "label": create_count_label(dept['name'], dept_count, dept_recommended_count),
                "value": f"dept_{dept['id']}",
                "children": []
            }
            
            for _, cat in dept_categories.iterrows():
                # Get subcategories for this category
                cat_subcats = subcategories[subcategories['category_id'] == cat['id']]
                cat_products = filtered_products[filtered_products['subcategory_id'].isin(cat_subcats['id'])]
                cat_count = len(cat_products)
                cat_recommended_count = len(cat_products[cat_products['status'] == 'recommended'])
                
                cat_node = {
                    "label": create_count_label(cat['name'], cat_count, cat_recommended_count),
                    "value": f"cat_{cat['id']}",
                    "children": []
                }
                
                for _, subcat in cat_subcats.iterrows():
                    # Get products for this subcategory (filtered)
                    subcat_products = filtered_products[filtered_products['subcategory_id'] == subcat['id']]
                    subcat_count = len(subcat_products)
                    subcat_recommended_count = len(subcat_products[subcat_products['status'] == 'recommended'])
                    
                    subcat_node = {
                        "label": create_count_label(subcat['name'], subcat_count, subcat_recommended_count),
                        "value": f"subcat_{subcat['id']}",
                        "children": []
                    }
                    
                    # Add individual products as children of subcategory with status indicators
                    for _, product in subcat_products.iterrows():
                        # Get status indicator emoji
                        status_emoji = get_status_indicator(product['status'])
                        
                        # Create product label with status indicator
                        if product['status'] == 'recommended':
                            label = f"{status_emoji} {product['name']} - ${product['price']:.2f} (RECOMMENDED)"
                        elif product['status'] == 'rejected':
                            label = f"{status_emoji} {product['name']} - ${product['price']:.2f} (REJECTED)"
                        else:  # approved
                            label = f"{status_emoji} {product['name']} - ${product['price']:.2f}"
                        
                        product_node = {
                            "label": label,
                            "value": f"product_{product['id']}"
                        }
                        subcat_node["children"].append(product_node)
                    
                    # Only add subcategory if it has products
                    if subcat_count > 0:
                        cat_node["children"].append(subcat_node)
                
                # Only add category if it has products  
                if cat_count > 0:
                    dept_node["children"].append(cat_node)
            
            # Only add department if it has products
            if dept_count > 0:
                tree_nodes.append(dept_node)
        
        return tree_nodes
    
    # Create tree nodes
    nodes = build_tree_nodes()
    
    # Display tree selector
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📋 Select Hierarchy Levels")
        return_select = tree_select(
            nodes,
            check_model="all",  # Allow selection at all levels (departments, categories, subcategories)
            expanded=["dept_1", "dept_2"],  # Expand first two departments by default
            no_cascade=False,  # Allow parent selection to cascade to children
            show_expand_all=True  # Show expand/collapse all buttons
        )
    
    with col2:
        st.markdown("### 📊 Quality Evolution Over Time")
        
        if return_select and return_select.get('checked'):
            selected_values = return_select['checked']
            
            # Parse selected IDs at all levels
            selected_dept_ids = []
            selected_cat_ids = []
            selected_subcat_ids = []
            selected_product_ids = []
            
            for value in selected_values:
                if value.startswith('dept_'):
                    dept_id = int(value.replace('dept_', ''))
                    selected_dept_ids.append(dept_id)
                elif value.startswith('cat_'):
                    cat_id = int(value.replace('cat_', ''))
                    selected_cat_ids.append(cat_id)
                elif value.startswith('subcat_'):
                    subcat_id = int(value.replace('subcat_', ''))
                    selected_subcat_ids.append(subcat_id)
                elif value.startswith('product_'):
                    product_id = int(value.replace('product_', ''))
                    selected_product_ids.append(product_id)
            
            # Build comprehensive product filter based on all selections
            all_relevant_product_ids = set()
            
            # Add products from direct product selections
            all_relevant_product_ids.update(selected_product_ids)
            
            # Add products from direct subcategory selections
            for subcat_id in selected_subcat_ids:
                subcat_products = products[products['subcategory_id'] == subcat_id]['id'].tolist()
                all_relevant_product_ids.update(subcat_products)
            
            # Add products from selected categories
            for cat_id in selected_cat_ids:
                cat_subcats = subcategories[subcategories['category_id'] == cat_id]['id'].tolist()
                cat_products = products[products['subcategory_id'].isin(cat_subcats)]['id'].tolist()
                all_relevant_product_ids.update(cat_products)
            
            # Add products from selected departments
            for dept_id in selected_dept_ids:
                dept_cats = categories[categories['department_id'] == dept_id]['id'].tolist()
                dept_subcats = subcategories[subcategories['category_id'].isin(dept_cats)]['id'].tolist()
                dept_products = products[products['subcategory_id'].isin(dept_subcats)]['id'].tolist()
                all_relevant_product_ids.update(dept_products)
            
            if all_relevant_product_ids:
                # Show selection summary
                col2_1, col2_2, col2_3 = st.columns(3)
                
                with col2_1:
                    total_selections = len(selected_dept_ids) + len(selected_cat_ids) + len(selected_subcat_ids) + len(selected_product_ids)
                    st.metric("Total Selections", total_selections)
                
                with col2_2:
                    st.metric("Relevant Products", len(all_relevant_product_ids))
                
                with col2_3:
                    # Calculate quality distribution for current period
                    current_quality = temporal_quality[
                        (temporal_quality['product_id'].isin(list(all_relevant_product_ids))) &
                        (temporal_quality['period_id'] == '2023-12')  # Latest period
                    ]
                    good_count = len(current_quality[current_quality['quality'] == 'good'])
                    st.metric("Current Good Quality", f"{good_count}")
                
                # Create and display quality distribution chart
                dist_chart = create_quality_distribution_chart(list(all_relevant_product_ids), temporal_quality)
                if dist_chart:
                    st.plotly_chart(dist_chart, use_container_width=True, config={'displayModeBar': False})
                
                # Show quality trend analysis
                st.markdown("#### 📈 Quality Trend Analysis")
                
                # Calculate quality trends
                filtered_temporal = temporal_quality[temporal_quality['product_id'].isin(list(all_relevant_product_ids))]
                
                if not filtered_temporal.empty:
                    quality_trends = (
                        filtered_temporal.groupby(['period_index', 'period_name', 'quality'])
                        .size()
                        .unstack(fill_value=0)
                        .reset_index()
                        .sort_values('period_index')  # Sort by chronological order
                    )
                    
                    # Show key insights
                    col_insight1, col_insight2 = st.columns(2)
                    
                    with col_insight1:
                        st.markdown("**📊 Quality Trends:**")
                        if 'good' in quality_trends.columns:
                            good_trend = quality_trends['good'].iloc[-1] - quality_trends['good'].iloc[0]
                            if good_trend > 0:
                                st.success(f"🟢 Good quality increased by {good_trend} products")
                            elif good_trend < 0:
                                st.error(f"🔴 Good quality decreased by {abs(good_trend)} products")
                            else:
                                st.info("🟡 Good quality remained stable")
                    
                    with col_insight2:
                        st.markdown("**🎯 Best/Worst Periods:**")
                        if 'good' in quality_trends.columns:
                            best_period = quality_trends.loc[quality_trends['good'].idxmax(), 'period_name']
                            worst_period = quality_trends.loc[quality_trends['good'].idxmin(), 'period_name']
                            st.info(f"🏆 Best: {best_period}")
                            st.warning(f"⚠️ Worst: {worst_period}")
                    
                    # Show detailed breakdown
                    with st.expander("📋 View Detailed Quality Data"):
                        st.dataframe(
                            quality_trends,
                            use_container_width=True,
                            hide_index=True
                        )
                else:
                    st.warning("No temporal quality data available for selected items")
            else:
                st.info("Select items from the tree to see quality evolution")
        else:
            st.info("No items selected. Use the tree on the left to explore the hierarchy.")
    
    # Additional insights section
    st.markdown('<h2 class="section-header">💡 Tree Insights</h2>', unsafe_allow_html=True)
    
    if return_select and return_select.get('checked'):
        selected_values = return_select['checked']
        
        # Analyze what's expanded vs selected
        expanded_values = return_select.get('expanded', [])
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🔽 Expanded Nodes")
            expanded_display = []
            for value in expanded_values:
                if value.startswith('dept_'):
                    dept_id = int(value.replace('dept_', ''))
                    dept_name = departments[departments['id'] == dept_id]['name'].iloc[0]
                    expanded_display.append(f"📁 {dept_name}")
                elif value.startswith('cat_'):
                    cat_id = int(value.replace('cat_', ''))
                    cat_name = categories[categories['id'] == cat_id]['name'].iloc[0]
                    expanded_display.append(f"📂 {cat_name}")
            
            if expanded_display:
                for item in expanded_display:
                    st.write(item)
            else:
                st.info("No nodes expanded")
        
        with col2:
            st.markdown("#### ✅ Selected Nodes")
            selected_display = []
            for value in selected_values:
                if value.startswith('dept_'):
                    dept_id = int(value.replace('dept_', ''))
                    dept_name = departments[departments['id'] == dept_id]['name'].iloc[0]
                    selected_display.append(f"🏢 {dept_name}")
                elif value.startswith('cat_'):
                    cat_id = int(value.replace('cat_', ''))
                    cat_name = categories[categories['id'] == cat_id]['name'].iloc[0]
                    selected_display.append(f"📂 {cat_name}")
                elif value.startswith('subcat_'):
                    subcat_id = int(value.replace('subcat_', ''))
                    subcat_name = subcategories[subcategories['id'] == subcat_id]['name'].iloc[0]
                    selected_display.append(f"🏷️ {subcat_name}")
                elif value.startswith('product_'):
                    product_id = int(value.replace('product_', ''))
                    product_name = products[products['id'] == product_id]['name'].iloc[0]
                    selected_display.append(f"🛒 {product_name}")
            
            if selected_display:
                for item in selected_display:
                    st.write(item)
            else:
                st.info("No items selected")

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
            
        if st.button("🌳 Tree Hierarchy", use_container_width=True,
                     type="primary" if st.session_state.current_page == 'Tree Hierarchy' else "secondary"):
            st.session_state.current_page = 'Tree Hierarchy'
            st.rerun()
    
    # Route to appropriate page
    if st.session_state.current_page == "Documentation":
        show_documentation()
    elif st.session_state.current_page == "Data Explorer":
        show_data_explorer()
    elif st.session_state.current_page == "Tree Hierarchy":
        show_tree_hierarchy()

if __name__ == "__main__":
    main() 