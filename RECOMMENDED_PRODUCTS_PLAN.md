# Recommended Products Feature - Implementation Plan

## 📋 **Current State Overview**

### **Existing Application**
- **Name**: Data Science UI Mockup Tool (Grocery Store Data Explorer)
- **Framework**: Streamlit with interactive hierarchy navigation
- **Data Structure**: 4-level hierarchy (Departments → Categories → Subcategories → Products)
- **Key Features**:
  - Documentation and architecture overview
  - Interactive data explorer with hierarchical filtering
  - Tree hierarchy with multi-level selection using `streamlit-tree-select`
  - Quality evolution charts with temporal analysis
  - CSV-based data storage (no database required)

### **Current Data Files**
```
data/
├── departments.csv      # 8 departments (Fresh Foods, Packaged Goods, etc.)
├── categories.csv       # 24 categories (Fruits, Vegetables, Dairy, etc.)
├── subcategories.csv    # 72 subcategories (Citrus Fruits, Leafy Greens, etc.)
├── products.csv         # 500+ individual products with pricing/inventory
└── temporal_quality.csv # Quality tracking over time periods
```

---

## 🎯 **Use Case & Requirements**

### **Business Problem**
- **Weekly Recommendations**: New grocery items are automatically suggested for the store
- **Manual Approval Process**: Recommendations should not auto-add to the live hierarchy
- **Batch Review Workflow**: Managers review recommendations every few months (not weekly)
- **Contextual Placement**: Users need to see where recommended items would appear in the hierarchy
- **Bulk Operations**: Ability to approve/reject multiple items efficiently

### **Core Requirements**
1. **Visual Integration**: Recommended products appear in-place within the hierarchy with visual indicators
2. **Toggle Visibility**: Show/hide recommended products as needed
3. **Approval Actions**: Individual and bulk approve/reject capabilities
4. **Contextual Review**: See products in their suggested hierarchy positions
5. **Audit Trail**: Track approval decisions and review history
6. **Data Persistence**: Maintain approval states between sessions

---

## 🏗️ **Technical Approach**

### **Design Philosophy**
- **In-Place Approval**: Recommended products are pre-placed in hierarchy with visual flags
- **Minimal UI Disruption**: Enhance existing tree interface rather than creating new workflows
- **Keep/Remove Decision**: Users decide whether to keep auto-placed recommendations
- **Visual Indicators**: Clear status badges for different product states

### **Recommended Architecture**
- **Enhanced Tree View**: Extend current `streamlit-tree-select` with status indicators
- **Status-Based Filtering**: Dynamic show/hide based on product approval state
- **CSV-Based State Management**: Add status columns to existing product data
- **Session State Tracking**: Maintain UI state for review sessions

---

## 📊 **Data Architecture Changes**

### **Enhanced Product Schema**
```python
# products.csv - Additional Columns:
- status: 'approved' | 'recommended' | 'rejected'  # Product approval state
- recommendation_date: datetime                     # When item was suggested
- reviewed_by: string                              # Who made the approval decision
- review_date: datetime                            # When decision was made
- recommendation_source: string                    # Source of recommendation (AI, manual, etc.)
```

### **New Data Files**
```
data/
├── approved_hierarchy/          # Current production data
│   ├── departments.csv
│   ├── categories.csv
│   ├── subcategories.csv
│   └── products.csv
├── workflow_tracking/          # Audit trail
│   ├── approval_history.csv    # Complete approval history
│   └── review_sessions.csv     # Manager review session tracking
└── temporal_quality.csv       # Existing quality data
```

### **Approval History Schema**
```python
# approval_history.csv:
- product_id: int
- product_name: string
- action: 'approved' | 'rejected' | 'deferred'
- previous_status: string
- new_status: string
- reviewed_by: string
- review_date: datetime
- hierarchy_path: string  # "Department > Category > Subcategory"
```

---

## 🎨 **UI/UX Design Approach**

### **Visual Status Indicators**
```python
# Tree Node Labels with Status:
"🔍 New Product Name (RECOMMENDED)"     # Pending recommendation
"✅ Approved Product Name"              # Approved for live hierarchy  
"❌ Rejected Product Name"              # Rejected (if showing rejected items)
"📦 Regular Product Name"               # Existing approved products
```

### **Filter Controls (Sidebar)**
```python
# User Controls:
show_recommended = st.checkbox("Show Recommended Products", value=True)
show_rejected = st.checkbox("Show Rejected Products", value=False)  
show_approved_only = st.checkbox("Show Only Approved Products", value=False)
review_mode = st.selectbox("Review Mode", ["All", "This Week", "This Month"])
```

### **Bulk Operations Interface**
```python
# Below Tree Selection:
if selected_recommended_products:
    st.subheader("📋 Review Selected Products")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("✅ Approve Selected ({count})")
    with col2:
        st.button("❌ Reject Selected ({count})")
    with col3:
        st.button("⏭️ Review Later")
```

---

## 🛠️ **Implementation Plan**

### **Phase 1: Basic In-Place Approval** ⏱️ *~1-2 weeks*
**Goal**: Get core approval workflow working with existing UI

#### **Tasks**:
1. **Data Schema Enhancement**
   - Add status columns to products.csv
   - Create sample recommended products data
   - Implement status filtering logic

2. **Visual Indicators**
   - Enhance tree building function with status badges
   - Add emoji/icon indicators for product states
   - Implement show/hide filtering

3. **Basic Approval Actions**
   - Individual product approval buttons
   - Update CSV files with status changes
   - Simple success/error feedback

#### **Deliverables**:
- Products display with status indicators in tree
- Toggle to show/hide recommended products
- Click-to-approve individual products
- CSV persistence of approval decisions

### **Phase 2: Bulk Operations** ⏱️ *~1 week*
**Goal**: Enable efficient bulk review and approval

#### **Tasks**:
1. **Multi-Select Enhancement**
   - Use existing tree selection for bulk operations
   - Filter selections by status type
   - Display selection summary

2. **Bulk Action Controls**
   - Approve/reject buttons for selected items
   - Confirmation dialogs for bulk actions
   - Progress indicators for large batches

3. **Review Session Management**
   - Save/resume review sessions
   - Track review progress
   - Session summary statistics

#### **Deliverables**:
- Select multiple recommended products
- Bulk approve/reject with confirmation
- Review session persistence

### **Phase 3: Advanced Features** ⏱️ *~2 weeks*
**Goal**: Professional workflow management capabilities

#### **Tasks**:
1. **Audit Trail System**
   - Complete approval history logging
   - Review session tracking
   - Decision attribution and timestamps

2. **Advanced Filtering**
   - Filter by recommendation date
   - Filter by recommendation source
   - Review mode (weekly/monthly batches)

3. **Analytics Dashboard**
   - Approval rate statistics
   - Review session analytics
   - Recommendation accuracy metrics

#### **Deliverables**:
- Complete audit trail
- Advanced filtering options
- Review analytics dashboard

### **Phase 4: Hierarchy Reorganization** ⏱️ *~2-3 weeks*
**Goal**: Allow reorganization of approved hierarchy structure

#### **Tasks**:
1. **Component Research & Selection**
   - Evaluate `streamlit-draggable-list` for level reorganization
   - Test `streamlit-flow` for workflow visualization
   - Prototype drag-and-drop hierarchy editing

2. **Reorganization Interface**
   - Level-by-level reorganization tools
   - Drag-and-drop between hierarchy levels
   - Move products between subcategories

3. **Change Management**
   - Track hierarchy changes
   - Approval workflow for structural changes
   - Rollback capabilities

#### **Deliverables**:
- Drag-and-drop reorganization tools
- Hierarchy change tracking
- Administrative approval for structural changes

---

## 🔧 **Component Recommendations**

### **Current Stack (Keep)**
- ✅ **streamlit-tree-select**: Perfect for current tree navigation
- ✅ **plotly**: Excellent for quality charts and analytics
- ✅ **pandas**: Solid data manipulation foundation
- ✅ **CSV storage**: Simple, reliable, version-controllable

### **Future Enhancements (Phase 4)**
- 🔄 **streamlit-draggable-list**: For level-by-level reorganization
- 🔄 **streamlit-flow**: Alternative for visual workflow management
- 🔄 **streamlit-agraph**: Option for complex hierarchy visualization

### **Avoid (Not Needed)**
- ❌ Complex workflow engines (overkill for this use case)
- ❌ Database systems (CSV approach works well)
- ❌ Custom drag-and-drop components (good pre-built options exist)

---

## 🚀 **Quick Start Strategy**

### **Immediate Next Steps**:
1. **Enhance products.csv** with status column
2. **Create sample recommended products** with status='recommended'
3. **Add filter toggle** in sidebar for recommended products
4. **Enhance tree labels** with status indicators
5. **Add basic approval buttons** below tree selection

### **Success Metrics**:
- ✅ Recommended products visible in tree with clear indicators
- ✅ Toggle successfully shows/hides recommended items
- ✅ Approval actions update product status
- ✅ Changes persist between app sessions
- ✅ Bulk operations work efficiently

### **Risk Mitigation**:
- **Start with existing tree component** (low risk, familiar UI)
- **CSV backup strategy** before any data changes
- **Incremental rollout** of features
- **Fallback to manual approval** if automation fails

---

## 💡 **Key Design Decisions**

### **Why In-Place Approval?**
- **Contextual Review**: See products in their intended hierarchy position
- **Familiar Interface**: Uses existing tree navigation users know
- **Minimal Learning Curve**: Enhance rather than replace current UI
- **Efficient Workflow**: No drag-and-drop complexity for basic approval

### **Why CSV-Based Storage?**
- **Simplicity**: No database setup or management
- **Version Control**: Easy to track changes in git
- **Backup & Recovery**: Simple file-based backups
- **Portability**: Works anywhere without infrastructure

### **Why Status-Based Filtering?**
- **Progressive Disclosure**: Show only relevant items
- **Cognitive Load Reduction**: Don't overwhelm with too many options
- **Workflow Flexibility**: Support different review styles
- **Performance**: Filter large datasets efficiently

---

## 📈 **Expected Benefits**

### **For Managers/Users**:
- **Efficient Review Process**: See recommendations in context
- **Bulk Operations**: Handle multiple items quickly
- **Clear Visual Feedback**: Obvious status indicators
- **Flexible Workflow**: Review at their own pace

### **For Development**:
- **Low Implementation Risk**: Build on existing, working code
- **Incremental Delivery**: Ship features progressively
- **Maintainable Codebase**: Enhance rather than rewrite
- **Future Flexibility**: Foundation for advanced features

### **For Business**:
- **Faster Product Updates**: Streamlined approval process
- **Better Decision Making**: Products shown in hierarchy context
- **Audit Compliance**: Complete approval history
- **Scalable Workflow**: Handle growing product catalogs

---

*This document serves as the comprehensive plan for implementing the recommended products approval workflow. Implementation will proceed in phases, with each phase building on the previous foundation while maintaining system stability and user familiarity.*