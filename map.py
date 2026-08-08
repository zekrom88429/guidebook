import folium

# 13 個地點資料
locations = [
    {"id": 1, "name": "V City", "coords": [22.3953572, 113.97403], "color": "#E63946"},
    {"id": 2, "name": "屯門時代廣場北翼 Tuen Mun Trend Plaza North Wing", "coords": [22.39315, 113.97574], "color": "#2A9D8F"},
    {"id": 3, "name": "屯門時代廣場南翼 Tuen Mun Trend Plaza South Wing", "coords": [22.3922, 113.9757], "color": "#F4A261"},
    {"id": 4, "name": "錦薈坊 K point", "coords": [22.39384, 113.9755], "color": "#9C27B0"},
    {"id": 5, "name": "屯門市廣場 二期 TmT Plaza phase 2", "coords": [22.39407, 113.97626], "color": "#E91E63"},
    {"id": 6, "name": "屯門市廣場 一期 TmT Plaza phase 1", "coords": [22.39286, 113.97719], "color": "#D32F2F"},
    {"id": 7, "name": "華都商場/華都大道 WALDORF SHOPPING CENTRE/ Waldorf Avenue", "coords": [22.39184, 113.97805], "color": "#F9C74F"},
    {"id": 8, "name": "新都 New Town Commercial Arcade", "coords": [22.39087, 113.9783], "color": "#277DA1"},
    {"id": 9, "name": "屯門站 Tuen Mun Station (MTR)", "coords": [22.39494, 113.97303], "color": "#1D3557"},
    {"id": 10, "name": "屯門站 Tuen Mun Station (Light Rail)", "coords": [22.3938, 113.97326], "color": "#457B9D"},
    {"id": 11, "name": "河田 Ho Tin Station (Light Rail)", "coords": [22.39740, 113.97313], "color": "#A8DADC"},
    {"id": 12, "name": "杯渡 Pui To Station (Light Rail)", "coords": [22.39461, 113.9768], "color": "#6A4C93"},
    {"id": 13, "name": "市中心 Town Centre Station (Light Rail)", "coords": [22.39141, 113.97498], "color": "#1982C4"},
]

# 步驟 1：使用 folium.Figure 建立明確的像素高度 (500px) 容器
fig = folium.Figure(width="100%", height="500px")

# 步驟 2：建立地圖並加入 Figure 容器中
m = folium.Map(
    location=[22.3925, 113.9762], 
    zoom_start=17, 
    tiles="OpenStreetMap"
).add_to(fig)

# 步驟 3：注入 CSS 覆蓋樣式，避免 iframe 高度被 100% 算成 0px
iframe_fix_css = """
<style>
    html, body, .folium-map, div[id^="map_"] {
        width: 100% !important;
        height: 500px !important;
        margin: 0 !important;
        padding: 0 !important;
        position: relative !important;
    }
</style>
"""
m.get_root().html.add_child(folium.Element(iframe_fix_css))

# 步驟 4：新增帶數字標籤的圓形 Marker
for loc in locations:
    icon_html = f"""
    <div style="
        background-color: {loc['color']};
        color: white;
        border-radius: 50%;
        width: 28px;
        height: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 14px;
        border: 2px solid white;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.4);
    ">{loc['id']}</div>
    """
    folium.Marker(
        location=loc["coords"],
        icon=folium.DivIcon(html=icon_html),
        popup=folium.Popup(f"<b>{loc['id']}. {loc['name']}</b>", max_width=250)
    ).add_to(m)

# 步驟 5：建立可折疊的圖例選單 (Legend)
legend_items_html = "".join(
    f"""
    <div style="display: flex; align-items: center; margin-bottom: 4px;">
        <span style="
            background-color: {loc['color']};
            color: white;
            border-radius: 50%;
            width: 18px;
            height: 18px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-size: 11px;
            font-weight: bold;
            margin-right: 8px;
            flex-shrink: 0;
        ">{loc['id']}</span>
        <span style="font-size: 12px; color: #333;">{loc['name']}</span>
    </div>
    """ for loc in locations
)

legend_html = f"""
<div style="
    position: fixed; 
    bottom: 25px; 
    left: 25px; 
    width: 320px;
    background-color: rgba(255, 255, 255, 0.95);
    z-index: 9999; 
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.25);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    overflow: hidden;
">
    <div onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'none' ? 'block' : 'none'; this.querySelector('span').textContent = this.nextElementSibling.style.display === 'none' ? '▶' : '▼';"
         style="font-weight: bold; font-size: 13px; padding: 10px 15px; color: #111; border-bottom: 1px solid #eee; cursor: pointer; user-select: none;">
        <span style="margin-right: 6px;">▼</span>地圖圖例 (Tuen Mun Malls & Stations)
    </div>
    <div style="padding: 10px 15px; max-height: 140px; overflow-y: auto;">
        {legend_items_html}
    </div>
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

# 保存 HTML 檔案
m.save("tuen_mun_real_map.html")
print("tuen_mun_real_map.html 已成功生成（已修正高度問題）！")