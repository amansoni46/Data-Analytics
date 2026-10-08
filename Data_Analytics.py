import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


# ============================================================
# SAMPLE DATA
# ============================================================

data = [
    ["2026-01-05", "Laptop", "Electronics", "North", 12, 720000, 90000],
    ["2026-01-08", "Smartphone", "Electronics", "West", 20, 500000, 65000],
    ["2026-01-12", "Headphones", "Accessories", "South", 35, 105000, 30000],
    ["2026-01-18", "Monitor", "Electronics", "East", 15, 225000, 40000],
    ["2026-01-22", "Keyboard", "Accessories", "West", 40, 80000, 22000],
    ["2026-02-03", "Laptop", "Electronics", "South", 10, 600000, 75000],
    ["2026-02-07", "Smartphone", "Electronics", "North", 25, 625000, 80000],
    ["2026-02-14", "Headphones", "Accessories", "West", 45, 135000, 38000],
    ["2026-02-20", "Monitor", "Electronics", "South", 18, 270000, 50000],
    ["2026-02-25", "Keyboard", "Accessories", "East", 50, 100000, 28000],
    ["2026-03-04", "Laptop", "Electronics", "West", 14, 840000, 105000],
    ["2026-03-10", "Smartphone", "Electronics", "East", 30, 750000, 95000],
    ["2026-03-15", "Headphones", "Accessories", "North", 50, 150000, 42000],
    ["2026-03-21", "Monitor", "Electronics", "West", 20, 300000, 55000],
    ["2026-03-27", "Keyboard", "Accessories", "South", 60, 120000, 35000],
    ["2026-04-03", "Laptop", "Electronics", "East", 16, 960000, 120000],
    ["2026-04-09", "Smartphone", "Electronics", "South", 28, 700000, 90000],
    ["2026-04-15", "Headphones", "Accessories", "West", 55, 165000, 45000],
    ["2026-04-21", "Monitor", "Electronics", "North", 22, 330000, 60000],
    ["2026-04-28", "Keyboard", "Accessories", "East", 65, 130000, 38000],
    ["2026-05-05", "Laptop", "Electronics", "South", 18, 1080000, 135000],
    ["2026-05-11", "Smartphone", "Electronics", "West", 32, 800000, 100000],
    ["2026-05-17", "Headphones", "Accessories", "North", 60, 180000, 50000],
    ["2026-05-23", "Monitor", "Electronics", "East", 25, 375000, 70000],
    ["2026-05-29", "Keyboard", "Accessories", "West", 70, 140000, 42000],
    ["2026-06-04", "Laptop", "Electronics", "North", 20, 1200000, 150000],
    ["2026-06-10", "Smartphone", "Electronics", "South", 35, 875000, 110000],
    ["2026-06-16", "Headphones", "Accessories", "East", 65, 195000, 55000],
    ["2026-06-22", "Monitor", "Electronics", "West", 28, 420000, 80000],
    ["2026-06-28", "Keyboard", "Accessories", "North", 75, 150000, 45000],
]

df = pd.DataFrame(
    data,
    columns=[
        "Date",
        "Product",
        "Category",
        "Region",
        "Units",
        "Revenue",
        "Profit"
    ]
)

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.strftime("%b")


# ============================================================
# APP CONFIGURATION
# ============================================================

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.CYBORG
    ],
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1"
        }
    ]
)

app.title = "Data Analytics Dashboard"


# ============================================================
# CUSTOM STYLES
# ============================================================

CARD_STYLE = {
    "borderRadius": "16px",
    "border": "1px solid rgba(255,255,255,0.08)",
    "backgroundColor": "#151a21",
    "boxShadow": "0 8px 25px rgba(0,0,0,0.25)",
    "height": "100%"
}

GRAPH_STYLE = {
    "backgroundColor": "#151a21",
    "borderRadius": "16px",
    "padding": "10px",
    "border": "1px solid rgba(255,255,255,0.08)"
}


# ============================================================
# KPI CARD
# ============================================================

def kpi_card(title, value, subtitle, icon):

    return dbc.Card(
        dbc.CardBody(
            [
                html.Div(
                    [
                        html.Div(
                            icon,
                            style={
                                "fontSize": "28px",
                                "marginBottom": "8px"
                            }
                        ),

                        html.Div(
                            title,
                            style={
                                "fontSize": "14px",
                                "color": "#9ca3af"
                            }
                        ),

                        html.H3(
                            value,
                            style={
                                "fontWeight": "700",
                                "marginTop": "5px",
                                "marginBottom": "4px"
                            }
                        ),

                        html.Small(
                            subtitle,
                            style={
                                "color": "#7dd3fc"
                            }
                        )
                    ]
                )
            ]
        ),
        style=CARD_STYLE
    )


# ============================================================
# HEADER
# ============================================================

header = dbc.Navbar(
    dbc.Container(
        [
            html.Div(
                [
                    html.H3(
                        "Data Analytics",
                        style={
                            "fontWeight": "700",
                            "marginBottom": "0"
                        }
                    ),

                    html.Small(
                        "Interactive Business Intelligence Dashboard",
                        style={
                            "color": "#9ca3af"
                        }
                    )
                ]
            ),

            dbc.Badge(
                "LIVE ANALYTICS",
                color="success",
                className="px-3 py-2"
            )
        ],
        fluid=True
    ),
    color="#10141a",
    dark=True,
    className="mb-4 py-3"
)


# ============================================================
# FILTERS
# ============================================================

filters = dbc.Card(
    dbc.CardBody(
        [
            html.H5(
                "Dashboard Filters",
                className="mb-3"
            ),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Label("Category"),

                            dcc.Dropdown(
                                id="category-filter",

                                options=[
                                    {
                                        "label": x,
                                        "value": x
                                    }
                                    for x in sorted(df["Category"].unique())
                                ],

                                value=list(df["Category"].unique()),

                                multi=True,

                                style={
                                    "color": "#111827"
                                }
                            )
                        ],

                        md=4
                    ),

                    dbc.Col(
                        [
                            dbc.Label("Region"),

                            dcc.Dropdown(
                                id="region-filter",

                                options=[
                                    {
                                        "label": x,
                                        "value": x
                                    }
                                    for x in sorted(df["Region"].unique())
                                ],

                                value=list(df["Region"].unique()),

                                multi=True,

                                style={
                                    "color": "#111827"
                                }
                            )
                        ],

                        md=4
                    ),

                    dbc.Col(
                        [
                            dbc.Label("Date Range"),

                            dcc.DatePickerRange(
                                id="date-filter",

                                min_date_allowed=df["Date"].min(),

                                max_date_allowed=df["Date"].max(),

                                start_date=df["Date"].min(),

                                end_date=df["Date"].max(),

                                display_format="DD MMM YYYY",

                                style={
                                    "width": "100%"
                                }
                            )
                        ],

                        md=4
                    )
                ]
            )
        ]
    ),
    style=CARD_STYLE,
    className="mb-4"
)


# ============================================================
# MAIN LAYOUT
# ============================================================

app.layout = dbc.Container(
    [
        header,

        filters,

        # KPI ROW
        dbc.Row(
            [
                dbc.Col(
                    id="revenue-card",
                    md=3,
                    className="mb-3"
                ),

                dbc.Col(
                    id="profit-card",
                    md=3,
                    className="mb-3"
                ),

                dbc.Col(
                    id="orders-card",
                    md=3,
                    className="mb-3"
                ),

                dbc.Col(
                    id="units-card",
                    md=3,
                    className="mb-3"
                )
            ]
        ),

        # FIRST CHART ROW
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.Graph(
                                id="revenue-chart",
                                config={
                                    "displayModeBar": True,
                                    "responsive": True
                                }
                            )
                        ),
                        style=GRAPH_STYLE
                    ),
                    md=8,
                    className="mb-4"
                ),

                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.Graph(
                                id="category-pie",
                                config={
                                    "displayModeBar": True,
                                    "responsive": True
                                }
                            )
                        ),
                        style=GRAPH_STYLE
                    ),
                    md=4,
                    className="mb-4"
                )
            ]
        ),

        # SECOND CHART ROW
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.Graph(
                                id="product-chart",
                                config={
                                    "displayModeBar": True,
                                    "responsive": True
                                }
                            )
                        ),
                        style=GRAPH_STYLE
                    ),
                    md=6,
                    className="mb-4"
                ),

                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.Graph(
                                id="region-chart",
                                config={
                                    "displayModeBar": True,
                                    "responsive": True
                                }
                            )
                        ),
                        style=GRAPH_STYLE
                    ),
                    md=6,
                    className="mb-4"
                )
            ]
        ),

        # THIRD CHART ROW
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            dcc.Graph(
                                id="profit-chart",
                                config={
                                    "displayModeBar": True,
                                    "responsive": True
                                }
                            )
                        ),
                        style=GRAPH_STYLE
                    ),
                    md=7,
                    className="mb-4"
                ),

                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5(
                                    "Business Insights",
                                    className="mb-3"
                                ),

                                html.Div(
                                    id="insights",
                                    style={
                                        "lineHeight": "1.8"
                                    }
                                )
                            ]
                        ),
                        style=CARD_STYLE
                    ),
                    md=5,
                    className="mb-4"
                )
            ]
        ),

        # DATA TABLE
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5(
                        "Detailed Sales Data",
                        className="mb-3"
                    ),

                    html.Div(
                        id="data-table",
                        style={
                            "overflowX": "auto"
                        }
                    )
                ]
            ),
            style=CARD_STYLE,
            className="mb-5"
        ),

        html.Div(
            [
                html.P(
                    "Built with Python • Dash • Plotly • Pandas",
                    style={
                        "textAlign": "center",
                        "color": "#6b7280",
                        "paddingBottom": "20px"
                    }
                )
            ]
        )
    ],

    fluid=True,

    style={
        "maxWidth": "1600px",
        "padding": "0 20px"
    }
)


# ============================================================
# CALLBACK
# ============================================================

@app.callback(
    [
        Output("revenue-card", "children"),
        Output("profit-card", "children"),
        Output("orders-card", "children"),
        Output("units-card", "children"),

        Output("revenue-chart", "figure"),
        Output("category-pie", "figure"),
        Output("product-chart", "figure"),
        Output("region-chart", "figure"),
        Output("profit-chart", "figure"),

        Output("insights", "children"),
        Output("data-table", "children")
    ],

    [
        Input("category-filter", "value"),
        Input("region-filter", "value"),
        Input("date-filter", "start_date"),
        Input("date-filter", "end_date")
    ]
)
def update_dashboard(
    selected_categories,
    selected_regions,
    start_date,
    end_date
):

    filtered = df.copy()

    # CATEGORY FILTER
    if selected_categories:
        filtered = filtered[
            filtered["Category"].isin(selected_categories)
        ]

    # REGION FILTER
    if selected_regions:
        filtered = filtered[
            filtered["Region"].isin(selected_regions)
        ]

    # DATE FILTER
    if start_date:
        filtered = filtered[
            filtered["Date"] >= pd.to_datetime(start_date)
        ]

    if end_date:
        filtered = filtered[
            filtered["Date"] <= pd.to_datetime(end_date)
        ]

    # ========================================================
    # KPI CALCULATIONS
    # ========================================================

    total_revenue = filtered["Revenue"].sum()

    total_profit = filtered["Profit"].sum()

    total_orders = len(filtered)

    total_units = filtered["Units"].sum()

    profit_margin = (
        (total_profit / total_revenue) * 100
        if total_revenue > 0
        else 0
    )

    # ========================================================
    # KPI CARDS
    # ========================================================

    revenue_card = kpi_card(
        "Total Revenue",
        f"₹{total_revenue:,.0f}",
        "Overall sales revenue",
        "💰"
    )

    profit_card = kpi_card(
        "Total Profit",
        f"₹{total_profit:,.0f}",
        f"{profit_margin:.1f}% profit margin",
        "📈"
    )

    orders_card = kpi_card(
        "Total Orders",
        f"{total_orders:,}",
        "Transactions recorded",
        "🛒"
    )

    units_card = kpi_card(
        "Units Sold",
        f"{total_units:,}",
        "Total products sold",
        "📦"
    )

    # ========================================================
    # REVENUE TREND
    # ========================================================

    monthly = (
        filtered
        .groupby("Month", sort=False)
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum")
        )
        .reset_index()
    )

    month_order = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ]

    monthly["Month"] = pd.Categorical(
        monthly["Month"],
        categories=month_order,
        ordered=True
    )

    monthly = monthly.sort_values("Month")

    revenue_fig = px.line(
        monthly,
        x="Month",
        y="Revenue",
        markers=True,
        title="Revenue Trend"
    )

    revenue_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#151a21",
        plot_bgcolor="#151a21",
        hovermode="x unified",
        margin=dict(l=20, r=20, t=55, b=20)
    )

    # ========================================================
    # CATEGORY PIE
    # ========================================================

    category_data = (
        filtered
        .groupby("Category")["Revenue"]
        .sum()
        .reset_index()
    )

    category_fig = px.pie(
        category_data,
        names="Category",
        values="Revenue",
        hole=0.55,
        title="Revenue by Category"
    )

    category_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#151a21",
        margin=dict(l=20, r=20, t=55, b=20)
    )

    # ========================================================
    # PRODUCT PERFORMANCE
    # ========================================================

    product_data = (
        filtered
        .groupby("Product")["Revenue"]
        .sum()
        .reset_index()
        .sort_values("Revenue", ascending=True)
    )

    product_fig = px.bar(
        product_data,
        x="Revenue",
        y="Product",
        orientation="h",
        title="Product Performance"
    )

    product_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#151a21",
        plot_bgcolor="#151a21",
        margin=dict(l=20, r=20, t=55, b=20)
    )

    # ========================================================
    # REGION PERFORMANCE
    # ========================================================

    region_data = (
        filtered
        .groupby("Region")["Revenue"]
        .sum()
        .reset_index()
        .sort_values("Revenue", ascending=False)
    )

    region_fig = px.bar(
        region_data,
        x="Region",
        y="Revenue",
        title="Revenue by Region"
    )

    region_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#151a21",
        plot_bgcolor="#151a21",
        margin=dict(l=20, r=20, t=55, b=20)
    )

    # ========================================================
    # PROFIT ANALYSIS
    # ========================================================

    profit_data = (
        filtered
        .groupby("Product")
        .agg(
            Revenue=("Revenue", "sum"),
            Profit=("Profit", "sum")
        )
        .reset_index()
    )

    profit_fig = px.bar(
        profit_data,
        x="Product",
        y=["Revenue", "Profit"],
        barmode="group",
        title="Revenue vs Profit"
    )

    profit_fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#151a21",
        plot_bgcolor="#151a21",
        margin=dict(l=20, r=20, t=55, b=20)
    )

    # ========================================================
    # AUTOMATIC INSIGHTS
    # ========================================================

    if not filtered.empty:

        best_product = (
            filtered.groupby("Product")["Revenue"]
            .sum()
            .idxmax()
        )

        best_region = (
            filtered.groupby("Region")["Revenue"]
            .sum()
            .idxmax()
        )

        best_category = (
            filtered.groupby("Category")["Revenue"]
            .sum()
            .idxmax()
        )

        highest_profit_product = (
            filtered.groupby("Product")["Profit"]
            .sum()
            .idxmax()
        )

        insights = [
            html.Div(
                [
                    html.Strong("🏆 Top Product: "),
                    f"{best_product}"
                ],
                className="mb-2"
            ),

            html.Div(
                [
                    html.Strong("🌎 Best Region: "),
                    f"{best_region}"
                ],
                className="mb-2"
            ),

            html.Div(
                [
                    html.Strong("📊 Leading Category: "),
                    f"{best_category}"
                ],
                className="mb-2"
            ),

            html.Div(
                [
                    html.Strong("💎 Highest Profit Product: "),
                    f"{highest_profit_product}"
                ],
                className="mb-2"
            ),

            html.Hr(),

            html.Div(
                [
                    html.Strong("💰 Profit Margin: "),
                    f"{profit_margin:.2f}%"
                ],
                className="mb-2"
            ),

            html.Div(
                [
                    html.Strong("📦 Average Order Units: "),
                    f"{total_units / total_orders:.1f}"
                    if total_orders > 0
                    else "0"
                ]
            )
        ]

    else:

        insights = html.Div(
            "No data available for selected filters.",
            style={"color": "#f87171"}
        )

    # ========================================================
    # DATA TABLE
    # ========================================================

    table_header = html.Thead(
        html.Tr(
            [
                html.Th("Date"),
                html.Th("Product"),
                html.Th("Category"),
                html.Th("Region"),
                html.Th("Units"),
                html.Th("Revenue"),
                html.Th("Profit")
            ]
        )
    )

    table_rows = []

    for _, row in filtered.sort_values(
        "Date",
        ascending=False
    ).head(15).iterrows():

        table_rows.append(
            html.Tr(
                [
                    html.Td(
                        row["Date"].strftime("%d %b %Y")
                    ),

                    html.Td(row["Product"]),

                    html.Td(row["Category"]),

                    html.Td(row["Region"]),

                    html.Td(f"{row['Units']:,}"),

                    html.Td(
                        f"₹{row['Revenue']:,.0f}"
                    ),

                    html.Td(
                        f"₹{row['Profit']:,.0f}"
                    )
                ]
            )
        )

    table = dbc.Table(
        [
            table_header,
            html.Tbody(table_rows)
        ],
        bordered=True,
        hover=True,
        responsive=True,
        striped=True,
        className="mb-0"
    )

    return (
        revenue_card,
        profit_card,
        orders_card,
        units_card,

        revenue_fig,
        category_fig,
        product_fig,
        region_fig,
        profit_fig,

        insights,
        table
    )


# ============================================================
# RUN APP
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)