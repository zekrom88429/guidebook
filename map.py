import folium

# 1. 屯門 8 大商場的真實經緯度座標與專屬顏色
locations = [
    {"id": 1, "name": "V City", "coords": [22.3953572, 113.97403], "color": "#E63946"},
    {"id": 2, "name": "屯門時代廣場北翼 Tuen Mun Trend Plaza North Wing", "coords": [22.39315, 113.97574], "color": "#2A9D8F"},
    {"id": 3, "name": "屯門時代廣場南翼 Tuen Mun Trend Plaza South Wing", "coords": [22.3922, 113.9757], "color": "#F4A261"},
    {"id": 4, "name": "錦薈坊 K point", "coords": [22.39384, 113.9755], "color": "#9C27B0"},
    {"id": 5, "name": "屯門市廣場 二期 TmT Plaza phase 2", "coords": [22.39407, 113.97626], "color": "#E91E63"},
    {"id": 6, "name": "屯門市廣場 一期 TmT Plaza phase 1", "coords": [22.39286, 113.97719], "color": "#D32F2F"},
    {"id": 7, "name": "華都商場/華都大道 WALDORF SHOPPING CENTRE/ Waldorf Avenue ", "coords": [22.39184,113.97805], "color": "#F9C74F"},
    {"id": 8, "name": "新都 New Town Commercial Arcade ", "coords": [22.39087, 113.9783], "color": "#277DA1"}
]

stations = [
    {"name": "Tuen Mun Station (MTR)", "coords": [22.39494, 113.97303], "type": "mtr"},
    {"name": "Tuen Mun Station (Light Rail)", "coords": [22.3938, 113.97326], "type": "lr"},
    {"name": "Ho Tin Station (Light Rail)", "coords": [22.39740, 113.97313], "type": "lr"},
    {"name": "Pui To Station (Light Rail)", "coords": [22.39461, 113.9768], "type": "lr"},
    {"name": "Town Centre Station (Light Rail)", "coords": [22.39141, 113.97498], "type": "lr"},
    
]


# 2. 以屯門市中心為原點建立真實地圖
m = folium.Map(location=[22.3925, 113.9762], zoom_start=17, tiles="OpenStreetMap")

# 3. 放置不同顏色、帶數字的圓圈 Marker
for loc in locations:
    # 建立 HTML 自訂圓圈數字圖示
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

# 4. 在圖片/地圖左下角嵌入 Legend (圖例)
legend_items_html = ""
for loc in locations:
    legend_items_html += f"""
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
    """

legend_html = f"""
<div style="
    position: fixed; 
    bottom: 25px; 
    left: 25px; 
    width: 310px;
    background-color: rgba(255, 255, 255, 0.95);
    z-index: 9999; 
    padding: 12px 15px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.25);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
">
    <div style="font-weight: bold; font-size: 13px; margin-bottom: 8px; color: #111; border-bottom: 1px solid #eee; padding-bottom: 4px;">
        地圖圖例 (Tuen Mun Malls)
    </div>
    {legend_items_html}
</div>
"""

m.get_root().html.add_child(folium.Element(legend_html))

# 5. 儲存地圖檔
m.save("tuen_mun_real_map.html")
print("地圖已生成！請雙擊打開 tuen_mun_real_map.html 檔案即可觀看正確地圖。")