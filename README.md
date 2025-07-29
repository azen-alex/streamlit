# 🛒 Data Science UI Mockup Tool

A simple Streamlit application designed to help data science teams mock up user interfaces with realistic hierarchical data. This tool uses a grocery store hierarchy as sample data to stress-test UX/UI designs.

## 🎯 Purpose

This application serves as a UI prototyping tool that provides:
- **Hierarchical Data Structure**: 4-level grocery store organization (Departments → Categories → Subcategories → Products)
- **Interactive Navigation**: Drill-down capabilities and filtering
- **Flat File Storage**: Simple CSV files for easy data modification
- **Non-Technical Friendly**: Web interface requiring no coding knowledge

## 🏗️ Architecture

The application follows a simple three-tier architecture:
1. **Presentation Layer**: Streamlit web interface
2. **Data Layer**: CSV files storing hierarchical grocery data
3. **Logic Layer**: Python scripts for data processing and visualization

## 📁 Project Structure

```
📁 Streamlit App
├── 📄 app.py                  # Main application file
├── 📄 requirements.txt        # Python dependencies
├── 📄 README.md              # This file
├── 📁 data/                  # Data storage directory
│   ├── 📄 departments.csv    # Level 1: Store departments
│   ├── 📄 categories.csv     # Level 2: Product categories  
│   ├── 📄 subcategories.csv  # Level 3: Product subcategories
│   └── 📄 products.csv       # Level 4: Individual products
└── 📁 scripts/              # Utility scripts
    └── 📄 generate_data.py   # Data generation script
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download this project**
   ```bash
   cd /path/to/your/project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate sample data**
   ```bash
   python scripts/generate_data.py
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   The app will automatically open at `http://localhost:8501`

## 📊 Data Structure

The application uses a 4-level hierarchical structure:

1. **Departments** (8 total): Major store sections
   - Fresh Foods, Packaged Goods, Frozen, Dairy & Eggs, etc.

2. **Categories** (24 total): Product groupings within departments
   - Fruits, Vegetables, Snacks, Beverages, etc.

3. **Subcategories** (72 total): Specific product types
   - Citrus Fruits, Leafy Greens, Chips & Crackers, etc.

4. **Products** (500+ total): Individual items with details
   - Name, price, stock quantity, unit of measure

## 🎨 Features

### Documentation Page
- **Architecture Diagrams**: Visual representation of system components
- **Data Structure**: Hierarchical organization explanation
- **Usage Guide**: Step-by-step instructions for non-technical users
- **Technical Details**: Implementation information

### Data Explorer Page
- **Overview Metrics**: Summary statistics of data hierarchy
- **Interactive Filters**: Drill-down navigation through hierarchy levels
- **Search Functionality**: Find products by name
- **Sorting Options**: Organize data by different criteria
- **Real-time Updates**: Dynamic filtering and display

## 🛠️ Customization

### Modifying Data
All data is stored in CSV files in the `data/` directory. You can:
- Edit files directly in Excel or any text editor
- Modify the `scripts/generate_data.py` to create different data sets
- Add or remove hierarchy levels by updating the data structure

### Extending Functionality
The modular design makes it easy to:
- Add new visualization components
- Implement additional filtering options
- Create new pages or sections
- Integrate with external data sources

## 🔧 Technical Implementation

### Technologies Used
- **Streamlit**: Web application framework for rapid prototyping
- **Pandas**: Data manipulation and analysis
- **Python**: Core programming language
- **Faker**: Realistic fake data generation
- **CSV**: Simple, portable data storage format

### Key Design Decisions
- **Zero Database**: Uses flat files for simplicity and portability
- **Hierarchical Structure**: Mimics real-world data relationships
- **Responsive Design**: Works on both desktop and mobile devices
- **Modular Code**: Easy to maintain and extend

## 🎯 Use Cases

This tool is perfect for:
- **UI/UX Prototyping**: Test interface designs with realistic data
- **Data Visualization**: Experiment with different chart types and layouts
- **User Testing**: Provide realistic data for user experience studies
- **Training**: Teach hierarchical data concepts to non-technical team members
- **Mockups**: Create demos for stakeholders and clients

## 🤝 Contributing

To extend this application:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Support

For questions or issues:
1. Check the Documentation page in the app
2. Review this README file
3. Examine the code comments in `app.py`
4. Modify the data files to experiment with different scenarios

---

**Happy prototyping!** 🚀 