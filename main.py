# -*- coding: utf-8 -*-
"""
🎨 مولد صور الأكواد v4.0 - الإصدار المتقدم
Developed by Muhammed Alaa © 2026
"""
from pywebio import start_server
from pywebio.input import (
    input, TEXT, textarea, select, radio, NUMBER, checkbox
)
from pywebio.output import (
    put_html, put_markdown, put_buttons, put_grid,
    put_info, put_warning, put_error, put_success,
    clear, toast, use_scope, put_collapse
)
from pywebio.session import set_env, run_js, go_app, local
import base64
import html as html_module
import random

# ═══════════════════════════════════════════════════════════
#                    🎨 الثيمات (25)
# ═══════════════════════════════════════════════════════════

THEMES = {
    "Monokai": {"bg": "#272822", "text": "#f8f8f2", "comment": "#75715e",
        "keyword": "#f92672", "string": "#e6db74", "number": "#ae81ff",
        "function": "#a6e22e", "class": "#66d9ef", "accent": "#fd971f",
        "window_bg": "#3e3d32"},
    "Dracula": {"bg": "#282a36", "text": "#f8f8f2", "comment": "#6272a4",
        "keyword": "#ff79c6", "string": "#f1fa8c", "number": "#bd93f9",
        "function": "#50fa7b", "class": "#8be9fd", "accent": "#bd93f9",
        "window_bg": "#44475a"},
    "One Dark Pro": {"bg": "#282c34", "text": "#abb2bf", "comment": "#5c6370",
        "keyword": "#c678dd", "string": "#98c379", "number": "#d19a66",
        "function": "#61afef", "class": "#e5c07b", "accent": "#61afef",
        "window_bg": "#21252b"},
    "GitHub Dark": {"bg": "#0d1117", "text": "#c9d1d9", "comment": "#8b949e",
        "keyword": "#ff7b72", "string": "#a5d6ff", "number": "#79c0ff",
        "function": "#d2a8ff", "class": "#ffa657", "accent": "#58a6ff",
        "window_bg": "#161b22"},
    "GitHub Light": {"bg": "#ffffff", "text": "#24292f", "comment": "#6e7781",
        "keyword": "#cf222e", "string": "#0a3069", "number": "#0550ae",
        "function": "#8250df", "class": "#953800", "accent": "#0969da",
        "window_bg": "#f6f8fa"},
    "VS Code Dark+": {"bg": "#1e1e1e", "text": "#d4d4d4", "comment": "#6a9955",
        "keyword": "#569cd6", "string": "#ce9178", "number": "#b5cea8",
        "function": "#dcdcaa", "class": "#4ec9b0", "accent": "#007acc",
        "window_bg": "#252526"},
    "Solarized Dark": {"bg": "#002b36", "text": "#839496", "comment": "#586e75",
        "keyword": "#859900", "string": "#2aa198", "number": "#d33682",
        "function": "#268bd2", "class": "#b58900", "accent": "#268bd2",
        "window_bg": "#073642"},
    "Solarized Light": {"bg": "#fdf6e3", "text": "#657b83", "comment": "#93a1a1",
        "keyword": "#859900", "string": "#2aa198", "number": "#d33682",
        "function": "#268bd2", "class": "#b58900", "accent": "#268bd2",
        "window_bg": "#eee8d5"},
    "Nord": {"bg": "#2e3440", "text": "#d8dee9", "comment": "#616e88",
        "keyword": "#81a1c1", "string": "#a3be8c", "number": "#b48ead",
        "function": "#88c0d0", "class": "#8fbcbb", "accent": "#88c0d0",
        "window_bg": "#3b4252"},
    "Gruvbox Dark": {"bg": "#282828", "text": "#ebdbb2", "comment": "#928374",
        "keyword": "#fb4934", "string": "#b8bb26", "number": "#d3869b",
        "function": "#b8bb26", "class": "#fabd2f", "accent": "#fabd2f",
        "window_bg": "#3c3836"},
    "Gruvbox Light": {"bg": "#fbf1c7", "text": "#3c3836", "comment": "#928374",
        "keyword": "#9d0006", "string": "#79740e", "number": "#8f3f71",
        "function": "#79740e", "class": "#b57614", "accent": "#b57614",
        "window_bg": "#ebdbb2"},
    "Tokyo Night": {"bg": "#1a1b26", "text": "#c0caf5", "comment": "#565f89",
        "keyword": "#bb9af7", "string": "#9ece6a", "number": "#ff9e64",
        "function": "#7aa2f7", "class": "#2ac3de", "accent": "#bb9af7",
        "window_bg": "#24283b"},
    "Catppuccin Mocha": {"bg": "#1e1e2e", "text": "#cdd6f4", "comment": "#6c7086",
        "keyword": "#cba6f7", "string": "#a6e3a1", "number": "#fab387",
        "function": "#89b4fa", "class": "#f9e2af", "accent": "#cba6f7",
        "window_bg": "#313244"},
    "Catppuccin Latte": {"bg": "#eff1f5", "text": "#4c4f69", "comment": "#9ca0b0",
        "keyword": "#8839ef", "string": "#40a02b", "number": "#fe640b",
        "function": "#1e66f5", "class": "#df8e1d", "accent": "#8839ef",
        "window_bg": "#e6e9ef"},
    "Material Ocean": {"bg": "#0f111a", "text": "#8f93a2", "comment": "#464b5d",
        "keyword": "#c792ea", "string": "#c3e88d", "number": "#f78c6c",
        "function": "#82aaff", "class": "#ffcb6b", "accent": "#82aaff",
        "window_bg": "#1a1f2e"},
    "Palenight": {"bg": "#292d3e", "text": "#a6accd", "comment": "#676e95",
        "keyword": "#c792ea", "string": "#c3e88d", "number": "#f78c6c",
        "function": "#82aaff", "class": "#ffcb6b", "accent": "#c792ea",
        "window_bg": "#1b1e2b"},
    "Synthwave 84": {"bg": "#262335", "text": "#ffffff", "comment": "#848bbd",
        "keyword": "#f92aad", "string": "#ff8b39", "number": "#f97e72",
        "function": "#36f9f6", "class": "#fede5d", "accent": "#f92aad",
        "window_bg": "#1e1c2f"},
    "Cyberpunk": {"bg": "#0d0221", "text": "#00ff9f", "comment": "#6c7086",
        "keyword": "#ff00ff", "string": "#ffff00", "number": "#00d9ff",
        "function": "#00ff9f", "class": "#ff00ff", "accent": "#ff00ff",
        "window_bg": "#1a0b2e"},
    "Ayu Mirage": {"bg": "#1f2430", "text": "#cbccc6", "comment": "#5c6773",
        "keyword": "#ffa759", "string": "#bae67e", "number": "#d4bfff",
        "function": "#ffd580", "class": "#73d0ff", "accent": "#ffa759",
        "window_bg": "#242936"},
    "Horizon": {"bg": "#1c1e26", "text": "#d5d8da", "comment": "#6c6f93",
        "keyword": "#e95678", "string": "#fadad1", "number": "#f09483",
        "function": "#fab795", "class": "#b877db", "accent": "#e95678",
        "window_bg": "#232530"},
    "Rosé Pine": {"bg": "#191724", "text": "#e0def4", "comment": "#6e6a86",
        "keyword": "#c4a7e7", "string": "#f6c177", "number": "#ebbcba",
        "function": "#9ccfd8", "class": "#31748f", "accent": "#ebbcba",
        "window_bg": "#1f1d2e"},
    "Night Owl": {"bg": "#011627", "text": "#d6deeb", "comment": "#637777",
        "keyword": "#c792ea", "string": "#ecc48d", "number": "#f78c6c",
        "function": "#82aaff", "class": "#ffcb8b", "accent": "#82aaff",
        "window_bg": "#0b2942"},
    "Bluloco Dark": {"bg": "#282c34", "text": "#abb2bf", "comment": "#5c6370",
        "keyword": "#c678dd", "string": "#98c379", "number": "#d19a66",
        "function": "#61afef", "class": "#e5c07b", "accent": "#61afef",
        "window_bg": "#21252b"},
    "Aurora X": {"bg": "#1a1a2e", "text": "#eaeaea", "comment": "#8d8daa",
        "keyword": "#e94560", "string": "#f6c177", "number": "#a8dadc",
        "function": "#4cc9f0", "class": "#f72585", "accent": "#e94560",
        "window_bg": "#16213e"},
    "Sunset": {"bg": "#2b1055", "text": "#f8f8f2", "comment": "#a09ebb",
        "keyword": "#ff79c6", "string": "#f1fa8c", "number": "#bd93f9",
        "function": "#50fa7b", "class": "#8be9fd", "accent": "#ff79c6",
        "window_bg": "#3a1a6b"},
}


# ═══════════════════════════════════════════════════════════
#                    🌈 الخلفيات
# ═══════════════════════════════════════════════════════════

BACKGROUNDS = {
    "بدون (لون الثيم)": {"type": "theme"},
    "أسود": {"type": "solid", "color": "#000000"},
    "أبيض": {"type": "solid", "color": "#ffffff"},
    "رمادي داكن": {"type": "solid", "color": "#1a1a1a"},
    "رمادي فاتح": {"type": "solid", "color": "#e0e0e0"},
    "أزرق داكن": {"type": "solid", "color": "#0a1929"},
    "بنفسجي": {"type": "solid", "color": "#4c1d95"},
    "أخضر": {"type": "solid", "color": "#065f46"},
    "أحمر": {"type": "solid", "color": "#7f1d1d"},
    "بني": {"type": "solid", "color": "#3e2723"},
    "تدرج الغروب": {"type": "linear", "c1": "#ff7e5f", "c2": "#feb47b"},
    "تدرج المحيط": {"type": "linear", "c1": "#2193b0", "c2": "#6dd5ed"},
    "تدرج الغابة": {"type": "linear", "c1": "#134e5e", "c2": "#71b280"},
    "تدرج الليل": {"type": "linear", "c1": "#0f2027", "c2": "#203a43"},
    "تدرج وردي": {"type": "linear", "c1": "#ee9ca7", "c2": "#ffdde1"},
    "تدرج ذهبي": {"type": "linear", "c1": "#f2994a", "c2": "#f2c94c"},
    "تدرج سماوي": {"type": "linear", "c1": "#56CCF2", "c2": "#2F80ED"},
    "تدرج بنفسجي": {"type": "linear", "c1": "#667eea", "c2": "#764ba2"},
    "تدرج أسود": {"type": "linear", "c1": "#000000", "c2": "#434343"},
    "تدرج زهري": {"type": "linear", "c1": "#ec008c", "c2": "#fc6767"},
    "نقش نقاط": {"type": "pattern", "pattern": "dots"},
    "نقش شبكة": {"type": "pattern", "pattern": "grid"},
    "نقش خطوط": {"type": "pattern", "pattern": "lines"},
}


# ═══════════════════════════════════════════════════════════
#                    📐 القوالب
# ═══════════════════════════════════════════════════════════

TEMPLATES = {
    "افتراضي": {"padding": 25, "font": 14, "radius": 12, "show_window": True},
    "بدون نافذة": {"padding": 20, "font": 14, "radius": 0, "show_window": False},
    "Twitter Post": {"padding": 40, "font": 16, "radius": 16, "show_window": True},
    "Instagram Square": {"padding": 50, "font": 16, "radius": 16, "show_window": True},
    "Instagram Story": {"padding": 60, "font": 18, "radius": 20, "show_window": True},
    "Facebook Post": {"padding": 40, "font": 16, "radius": 16, "show_window": True},
    "YouTube Thumbnail": {"padding": 40, "font": 18, "radius": 16, "show_window": True},
    "بطاقة عمل": {"padding": 30, "font": 14, "radius": 12, "show_window": False},
    "عرض تقديمي": {"padding": 60, "font": 20, "radius": 20, "show_window": True},
    "شاشة كاملة": {"padding": 80, "font": 22, "radius": 24, "show_window": True},
}


# ═══════════════════════════════════════════════════════════
#                    💻 اللغات
# ═══════════════════════════════════════════════════════════

LANGUAGES = {
    "Python": {
        "keywords": {'False','None','True','and','as','assert','async','await',
            'break','class','continue','def','del','elif','else','except',
            'finally','for','from','global','if','import','in','is',
            'lambda','nonlocal','not','or','pass','raise','return','try',
            'while','with','yield','self'},
        "builtins": {'print','len','range','str','int','float','list','dict',
            'set','tuple','bool','input','type','sum','max','min',
            'sorted','enumerate','zip','map','filter','abs','round',
            'all','any','open','isinstance'},
        "comment": "#", "strings": ['"', "'"], "filename": "main.py"},
    "JavaScript": {
        "keywords": {'var','let','const','function','return','if','else','for',
            'while','do','switch','case','break','continue','new','this',
            'class','extends','super','try','catch','finally','throw',
            'typeof','instanceof','in','of','null','undefined','true',
            'false','async','await','yield','import','export','from','default'},
        "builtins": {'console','Math','JSON','Object','Array','String',
            'Number','Boolean','Date','Promise','Map','Set'},
        "comment": "//", "strings": ['"', "'", '`'], "filename": "main.js"},
    "TypeScript": {
        "keywords": {'let','const','var','function','return','if','else','for',
            'while','do','switch','case','break','continue','new','this',
            'class','extends','super','interface','type','enum','implements',
            'public','private','protected','readonly','abstract','as','is',
            'null','undefined','true','false','async','await','import',
            'export','from','default'},
        "builtins": {'console','Math','JSON','Object','Array','String',
            'Number','Boolean','Date','Promise','Map','Set'},
        "comment": "//", "strings": ['"', "'", '`'], "filename": "main.ts"},
    "HTML": {
        "keywords": set(), "builtins": set(),
        "comment": "<!--", "strings": ['"', "'"], "filename": "index.html"},
    "CSS": {
        "keywords": {'important','media','import','keyframes','font-face'},
        "builtins": set(),
        "comment": "/*", "strings": ['"', "'"], "filename": "style.css"},
    "JSON": {
        "keywords": {'true','false','null'}, "builtins": set(),
        "comment": "//", "strings": ['"'], "filename": "data.json"},
    "SQL": {
        "keywords": {'SELECT','FROM','WHERE','INSERT','INTO','VALUES','UPDATE',
            'SET','DELETE','CREATE','TABLE','DROP','ALTER','JOIN','LEFT',
            'RIGHT','INNER','ON','GROUP','BY','ORDER','HAVING','LIMIT',
            'AS','AND','OR','NOT','NULL','IS','IN','BETWEEN','LIKE','DISTINCT'},
        "builtins": set(),
        "comment": "--", "strings": ["'"], "filename": "query.sql"},
    "Bash": {
        "keywords": {'if','then','else','elif','fi','for','while','do','done',
            'case','esac','function','return','break','continue','in',
            'echo','export','source','read','local','exit','cd','pwd','ls'},
        "builtins": {'echo','printf','read','cd','ls','pwd','mkdir','rm',
            'cat','grep','sed','awk','find','chmod'},
        "comment": "#", "strings": ['"', "'"], "filename": "script.sh"},
    "Java": {
        "keywords": {'public','private','protected','class','interface','extends',
            'implements','static','final','abstract','return','if','else',
            'for','while','do','switch','case','break','continue','new',
            'this','super','try','catch','finally','throw','throws','import',
            'package','void','int','long','double','float','boolean','char',
            'String','null','true','false','enum'},
        "builtins": {'System','String','Integer','Double','Math','Object'},
        "comment": "//", "strings": ['"', "'"], "filename": "Main.java"},
    "C++": {
        "keywords": {'int','char','double','float','bool','void','long','short',
            'unsigned','signed','const','static','extern','inline','virtual',
            'class','struct','union','enum','namespace','using','public',
            'private','protected','return','if','else','for','while','do',
            'switch','case','break','continue','new','delete','this',
            'try','catch','throw','template','auto','nullptr','true','false'},
        "builtins": {'cout','cin','endl','std','string','vector','map','set'},
        "comment": "//", "strings": ['"', "'"], "filename": "main.cpp"},
    "PHP": {
        "keywords": {'function','class','interface','extends','implements',
            'public','private','protected','static','const','var','return',
            'if','else','elseif','for','foreach','while','do','switch',
            'case','break','continue','new','this','try','catch','finally',
            'throw','use','namespace','echo','print','true','false','null'},
        "builtins": {'echo','print','array','count','strlen','substr'},
        "comment": "//", "strings": ['"', "'"], "filename": "index.php"},
    "Go": {
        "keywords": {'package','import','func','var','const','type','struct',
            'interface','map','chan','go','defer','return','if','else',
            'for','switch','case','break','continue','range','true','false','nil'},
        "builtins": {'println','printf','make','new','len','cap','append'},
        "comment": "//", "strings": ['"', '`'], "filename": "main.go"},
    "Rust": {
        "keywords": {'fn','let','mut','const','static','struct','enum','trait',
            'impl','pub','use','mod','crate','self','super','return','if',
            'else','match','for','while','loop','break','continue','in','as'},
        "builtins": {'println','print','vec','String','Box','Option','Result'},
        "comment": "//", "strings": ['"'], "filename": "main.rs"},
    "Ruby": {
        "keywords": {'def','end','class','module','if','elsif','else','unless',
            'while','until','for','do','case','when','then','begin','rescue',
            'ensure','return','yield','break','next','self','nil','true','false'},
        "builtins": {'puts','print','p','gets','require'},
        "comment": "#", "strings": ['"', "'"], "filename": "main.rb"},
    "YAML": {
        "keywords": {'true','false','null','yes','no'}, "builtins": set(),
        "comment": "#", "strings": ['"', "'"], "filename": "config.yaml"},
}


# ═══════════════════════════════════════════════════════════
#                    🎨 التلوين
# ═══════════════════════════════════════════════════════════

def esc(t):
    return html_module.escape(t)


def find_comment(line, comment_char, quote_chars):
    in_str = None
    i = 0
    while i < len(line):
        ch = line[i]
        if in_str:
            if ch == '\\' and i + 1 < len(line):
                i += 2
                continue
            if ch == in_str:
                in_str = None
        else:
            if ch in quote_chars:
                in_str = ch
            elif line[i:i+len(comment_char)] == comment_char:
                return i
        i += 1
    return -1


def highlight_code_part(line, theme, lang):
    result = ""
    i = 0
    n = len(line)
    keywords = lang["keywords"]
    builtins = lang["builtins"]
    quotes = lang["strings"]

    while i < n:
        ch = line[i]

        if ch in quotes:
            quote = ch
            j = i + 1
            while j < n:
                if line[j] == quote and line[j-1] != '\\':
                    break
                j += 1
            if j < n:
                j += 1
            result += f'<tspan fill="{theme["string"]}">{esc(line[i:j])}</tspan>'
            i = j
            continue

        if ch.isdigit():
            j = i
            while j < n and (line[j].isdigit() or line[j] in '.xXbBoOabcdef_'):
                j += 1
            result += f'<tspan fill="{theme["number"]}">{esc(line[i:j])}</tspan>'
            i = j
            continue

        if ch.isalpha() or ch == '_':
            j = i
            while j < n and (line[j].isalnum() or line[j] == '_'):
                j += 1
            word = line[i:j]
            wl = word.lower()
            wu = word.upper()

            if word in keywords or wl in keywords or wu in keywords:
                result += f'<tspan fill="{theme["keyword"]}" font-weight="bold">{esc(word)}</tspan>'
            elif word in builtins:
                result += f'<tspan fill="{theme["function"]}">{esc(word)}</tspan>'
            elif j < n and line[j] == '(':
                result += f'<tspan fill="{theme["function"]}">{esc(word)}</tspan>'
            elif word[0].isupper():
                result += f'<tspan fill="{theme["class"]}">{esc(word)}</tspan>'
            else:
                result += f'<tspan fill="{theme["text"]}">{esc(word)}</tspan>'
            i = j
            continue

        if ch in '+-*/%=<>!&|^~':
            j = i + 1
            while j < n and line[j] in '+-*/%=<>!&|^~':
                j += 1
            result += f'<tspan fill="{theme["keyword"]}">{esc(line[i:j])}</tspan>'
            i = j
            continue

        result += esc(ch)
        i += 1

    return result


def highlight_line(line, theme, lang):
    if not line.strip():
        return ""

    comment_char = lang["comment"]
    idx = find_comment(line, comment_char, lang["strings"])
    if idx != -1:
        return highlight_code_part(line[:idx], theme, lang) + \
               f'<tspan fill="{theme["comment"]}" font-style="italic">{esc(line[idx:])}</tspan>'

    return highlight_code_part(line, theme, lang)


# ═══════════════════════════════════════════════════════════
#                    🖼️ توليد SVG المتقدم
# ═══════════════════════════════════════════════════════════

def wrap_text(text, max_chars_per_line):
    """تقسيم النص الطويل إلى أسطر"""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= max_chars_per_line:
            current += (" " if current else "") + word
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def generate_svg(code, theme_name, lang_name, bg_name, template_name,
                watermark, show_numbers, filename,
                title="", description="", author="", version="",
                show_date=False, show_header=True, show_glow=False,
                show_border=False, border_color=""):
    """توليد SVG متقدم"""

    theme = THEMES.get(theme_name, THEMES["Monokai"])
    lang = LANGUAGES.get(lang_name, LANGUAGES["Python"])
    tpl = TEMPLATES.get(template_name, TEMPLATES["افتراضي"])
    bg = BACKGROUNDS.get(bg_name, {"type": "theme"})

    lines = code.split('\n')
    num_lines = len(lines)
    max_len = max((len(l) for l in lines), default=1)

    font = tpl["font"]
    line_h = int(font * 1.7)
    char_w = font * 0.62
    header_h = 45 if tpl["show_window"] else 0
    pad = tpl["padding"]

    # ═══ حساب الأبعاد ═══
    code_w = int(max_len * char_w) + pad * 2 + 80
    code_h = num_lines * line_h + pad * 2 + header_h

    # عنوان + وصف أعلى
    title_h = 0
    if title.strip():
        title_h += 50
    if author.strip() or version.strip() or show_date:
        title_h += 30

    # وصف أسفل
    desc_h = 0
    desc_lines = []
    if description.strip():
        max_chars = max(int((code_w - pad * 2) / (font * 0.55)), 30)
        desc_lines = wrap_text(description, max_chars)
        desc_h = len(desc_lines) * (font + 6) + 60

    outer_pad = 25
    W = max(code_w + outer_pad * 2, 500)
    H = code_h + outer_pad * 2 + title_h + desc_h

    # ═══ الخلفية ═══
    bg_defs = ""
    bg_fill = theme["bg"]

    if bg["type"] == "solid":
        bg_fill = bg["color"]
    elif bg["type"] == "linear":
        bg_defs = f'''<linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{bg["c1"]}"/>
            <stop offset="100%" stop-color="{bg["c2"]}"/>
        </linearGradient>'''
        bg_fill = "url(#bgGrad)"
    elif bg["type"] == "pattern":
        pattern = bg["pattern"]
        if pattern == "dots":
            bg_defs = f'<pattern id="bgPat" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="1.5" fill="{theme["accent"]}" opacity="0.15"/></pattern>'
        elif pattern == "grid":
            bg_defs = f'<pattern id="bgPat" x="0" y="0" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M 30 0 L 0 0 0 30" fill="none" stroke="{theme["accent"]}" stroke-width="1" opacity="0.15"/></pattern>'
        elif pattern == "lines":
            bg_defs = f'<pattern id="bgPat" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="20" y2="20" stroke="{theme["accent"]}" stroke-width="1" opacity="0.15"/></pattern>'

    # ═══ SVG ═══
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Consolas,Monaco,monospace">')
    parts.append('<defs>')
    parts.append(bg_defs)

    # توهج
    if show_glow:
        parts.append(f'<filter id="glow" x="-50%" y="-50%" width="200%" height="200%">')
        parts.append(f'<feGaussianBlur stdDeviation="8" result="coloredBlur"/>')
        parts.append(f'<feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>')
        parts.append('</filter>')

    # ظل
    parts.append('<filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">')
    parts.append('<feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000" flood-opacity="0.4"/>')
    parts.append('</filter>')

    parts.append('</defs>')

    # خلفية
    parts.append(f'<rect width="{W}" height="{H}" fill="{bg_fill}"/>')
    if bg["type"] == "pattern":
        parts.append(f'<rect width="{W}" height="{H}" fill="url(#bgPat)"/>')

    # ═══ العنوان أعلى ═══
    y_offset = outer_pad
    if title.strip():
        parts.append(f'<text x="{W // 2}" y="{y_offset + 30}" text-anchor="middle" '
                    f'fill="{theme["text"]}" font-size="22" font-weight="bold" '
                    f'font-family="Arial,sans-serif">{esc(title)}</text>')
        y_offset += 50

    if author.strip() or version.strip() or show_date:
        meta_parts = []
        if author.strip():
            meta_parts.append(f"👤 {author}")
        if version.strip():
            meta_parts.append(f"v{version}")
        if show_date:
            from datetime import datetime
            meta_parts.append(f"📅 {datetime.now().strftime('%Y-%m-%d')}")
        meta_text = " • ".join(meta_parts)
        parts.append(f'<text x="{W // 2}" y="{y_offset + 18}" text-anchor="middle" '
                    f'fill="{theme["accent"]}" font-size="13" '
                    f'font-family="Arial,sans-serif" opacity="0.9">{esc(meta_text)}</text>')
        y_offset += 30

    # ═══ بطاقة الكود ═══
    cx = outer_pad
    cy = y_offset
    cw = W - outer_pad * 2
    ch = code_h
    radius = tpl["radius"]

    # حدود
    if show_border:
        border = border_color if border_color else theme["accent"]
        parts.append(f'<rect x="{cx - 3}" y="{cy - 3}" width="{cw + 6}" height="{ch + 6}" '
                    f'rx="{radius + 3}" fill="none" stroke="{border}" stroke-width="3" '
                    + ('filter="url(#glow)"' if show_glow else '') + '/>')

    # ظل البطاقة
    parts.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="{radius}" '
                f'fill="{theme["bg"]}" filter="url(#shadow)"/>')

    # ═══ شريط العنوان ═══
    if tpl["show_window"]:
        header_bg = theme["window_bg"]
        parts.append(f'<path d="M {cx} {cy + radius} Q {cx} {cy} {cx + radius} {cy} L {cx + cw - radius} {cy} Q {cx + cw} {cy} {cx + cw} {cy + radius} L {cx + cw} {cy + header_h} L {cx} {cy + header_h} Z" fill="{header_bg}"/>')
        parts.append(f'<line x1="{cx}" y1="{cy + header_h}" x2="{cx + cw}" y2="{cy + header_h}" '
                    f'stroke="{theme["comment"]}" stroke-width="1" opacity="0.3"/>')

        # دوائر Mac
        hcy = cy + header_h // 2
        parts.append(f'<circle cx="{cx + 20}" cy="{hcy}" r="6" fill="#ff5f56"/>')
        parts.append(f'<circle cx="{cx + 42}" cy="{hcy}" r="6" fill="#ffbd2e"/>')
        parts.append(f'<circle cx="{cx + 64}" cy="{hcy}" r="6" fill="#27c93f"/>')

        # اسم الملف
        display_fn = filename.strip() if filename.strip() else lang.get("filename", "code.txt")
        parts.append(f'<text x="{W // 2}" y="{hcy + 5}" text-anchor="middle" '
                    f'fill="{theme["text"]}" font-size="13" opacity="0.75">{esc(display_fn)}</text>')

        # اسم اللغة
        parts.append(f'<text x="{cx + cw - 20}" y="{hcy + 5}" text-anchor="end" '
                    f'fill="{theme["accent"]}" font-size="12" font-weight="bold" '
                    f'opacity="0.9">{esc(lang_name)}</text>')

    # ═══ الكود ═══
    y_start = cy + header_h + pad + font
    for idx, line in enumerate(lines):
        y_pos = y_start + idx * line_h
        if y_pos > cy + ch - pad // 2:
            break

        if show_numbers:
            parts.append(f'<text x="{cx + pad + 30}" y="{y_pos}" text-anchor="end" '
                        f'fill="{theme["comment"]}" font-size="{font}" opacity="0.5">{idx + 1}</text>')
            tx = cx + pad + 50
        else:
            tx = cx + pad + 10

        hl = highlight_line(line, theme, lang)
        if hl:
            parts.append(f'<text x="{tx}" y="{y_pos}" font-size="{font}" '
                        f'fill="{theme["text"]}" xml:space="preserve">{hl}</text>')

    # ═══ الوصف تحت الصورة ═══
    if description.strip():
        dy = cy + ch + 30
        # خلفية الوصف
        desc_box_h = len(desc_lines) * (font + 6) + 40
        parts.append(f'<rect x="{cx}" y="{dy - 10}" width="{cw}" height="{desc_box_h}" '
                    f'rx="8" fill="{theme["window_bg"]}" opacity="0.9"/>')

        # ايقونة
        parts.append(f'<text x="{cx + 20}" y="{dy + 15}" fill="{theme["accent"]}" '
                    f'font-size="16" font-family="Arial">📝</text>')

        # نص الوصف
        for i, dline in enumerate(desc_lines):
            ly = dy + 15 + i * (font + 6)
            parts.append(f'<text x="{cx + 45}" y="{ly}" fill="{theme["text"]}" '
                        f'font-size="{font}" font-family="Arial,sans-serif" '
                        f'xml:space="preserve">{esc(dline)}</text>')

    # ═══ علامة مائية ═══
    if watermark.strip():
        parts.append(f'<text x="{W - 25}" y="{H - 15}" text-anchor="end" '
                    f'fill="{theme["text"]}" font-size="12" opacity="0.5" '
                    f'font-style="italic">{esc(watermark)}</text>')

    parts.append('</svg>')
    return ''.join(parts), W, H


# ═══════════════════════════════════════════════════════════
#                    🎨 الواجهة
# ═══════════════════════════════════════════════════════════

def setup_site():
    set_env(title="🎨 مولد صور الأكواد", auto_scroll_bottom=True)
    run_js('''var o=document.querySelector("link[rel*='icon']");if(o)o.remove();
    var i=document.createElement('link');i.rel='shortcut icon';
    i.href='https://cdn-icons-png.flaticon.com/512/1159/1159641.png';
    document.head.appendChild(i);''')


def render_header():
    put_html('''<div style="background:linear-gradient(135deg,#667eea,#764ba2);
        padding:25px;border-radius:15px;margin-bottom:20px;text-align:center;
        box-shadow:0 10px 30px rgba(0,0,0,0.2);color:white;">
    <h1 style="color:white;margin:0;font-size:30px;">🎨 مولد صور الأكواد v4.0</h1>
    <p style="margin:10px 0 0 0;opacity:0.95;font-size:14px;">
        25 ثيماً • 15 لغة • 10 قوالب • 22 خلفية • شرح مرفق</p>
    </div>''')


def render_footer():
    put_html('''<div style="text-align:center;padding:20px;margin-top:25px;
                color:#888;border-top:1px solid #e0e0e0;font-size:12px;">
    🎨 مولد صور الأكواد v4.0 |
    Developed by <b style="color:#667eea;">Muhammed Alaa © 2026</b>
    </div>''')


# ═══════════════════════════════════════════════════════════
#                    🎯 التطبيق
# ═══════════════════════════════════════════════════════════

def main():
    setup_site()
    clear()
    render_header()

    # ═══ 1. الكود ═══
    put_markdown("## 1️⃣ الكود")
    code = textarea(
        "الكود:",
        value='''def greet(name):
    print(f"مرحباً {name}!")

greet("أحمد")''',
        rows=12,
        code={'mode': 'python'},
        placeholder="الصق كودك هنا..."
    )

    # ═══ 2. الوصف ═══
    put_markdown("## 2️⃣ الشرح والوصف")
    title = input("🏷️ عنوان (اختياري):", type=TEXT, value="",
                 required=False, placeholder="مثال: دالة الترحيب")
    description = textarea(
        "📝 شرح الكود (يظهر تحت الصورة):",
        rows=3,
        value="",
        placeholder="اكتب شرحاً لوظيفة الكود... مثال: هذه الدالة تستقبل اسم المستخدم وتطبع رسالة ترحيب"
    )

    # ═══ 3. معلومات إضافية ═══
    with put_collapse("ℹ️ معلومات إضافية (اختياري)"):
        author = input("👤 المؤلف:", type=TEXT, value="",
                      required=False, placeholder="اسمك")
        version = input("🔢 الإصدار:", type=TEXT, value="",
                       required=False, placeholder="1.0")
        show_date = radio("📅 إظهار التاريخ:",
                        options=["لا", "نعم"],
                        value="لا", required=True, inline=True)

    # ═══ 4. التصميم ═══
    put_markdown("## 3️⃣ التصميم")

    lang_name = select("💻 اللغة:",
                      options=list(LANGUAGES.keys()),
                      value="Python", required=True)
    theme_name = select("🎨 الثيم:",
                       options=list(THEMES.keys()),
                       value="Monokai", required=True)
    bg_name = select("🌈 الخلفية:",
                    options=list(BACKGROUNDS.keys()),
                    value="بدون (لون الثيم)", required=True)
    template_name = select("📐 القالب:",
                          options=list(TEMPLATES.keys()),
                          value="افتراضي", required=True)

    # ═══ 5. تأثيرات بصرية ═══
    with put_collapse("✨ تأثيرات بصرية متقدمة (اختياري)"):
        show_glow = radio("🌟 توهج حول البطاقة:",
                        options=["لا", "نعم"],
                        value="لا", required=True, inline=True)
        show_border = radio("🔲 إطار ملون:",
                          options=["لا", "نعم"],
                          value="لا", required=True, inline=True)
        border_color = input("🎨 لون الإطار (hex):",
                           type=TEXT, value="#667eea",
                           required=False, placeholder="#667eea")

    # ═══ 6. تفاصيل ═══
    put_markdown("## 4️⃣ تفاصيل إضافية")

    filename = input("📄 اسم الملف:",
                    type=TEXT, value="",
                    required=False, placeholder="مثال: app.py")
    watermark = input("💧 علامة مائية:",
                     type=TEXT, value="",
                     required=False, placeholder="مثال: @username")
    show_numbers = radio("🔢 أرقام الأسطر:",
                        options=["نعم", "لا"],
                        value="نعم", required=True, inline=True)

    # ═══ توليد ═══
    put_markdown("---")
    put_buttons(
        ['🎨 توليد الصورة'],
        onclick=[lambda: do_generate(
            code=code,
            theme_name=theme_name,
            lang_name=lang_name,
            bg_name=bg_name,
            template_name=template_name,
            watermark=watermark,
            show_numbers=(show_numbers == "نعم"),
            filename=filename,
            title=title,
            description=description,
            author=author,
            version=version,
            show_date=(show_date == "نعم"),
            show_glow=(show_glow == "نعم"),
            show_border=(show_border == "نعم"),
            border_color=border_color,
        )]
    )

    use_scope('preview', clear=True)
    render_footer()


def do_generate(**kwargs):
    """توليد الصورة"""
    code = kwargs['code']

    if not code.strip():
        toast("⚠️ الرجاء إدخال كود!", color='warning')
        return

    clear('preview')
    with use_scope('preview'):
        put_markdown("---")
        put_markdown("## 🖼️ النتيجة")

        try:
            svg_str, w, h = generate_svg(
                code=kwargs['code'],
                theme_name=kwargs['theme_name'],
                lang_name=kwargs['lang_name'],
                bg_name=kwargs['bg_name'],
                template_name=kwargs['template_name'],
                watermark=kwargs['watermark'],
                show_numbers=kwargs['show_numbers'],
                filename=kwargs['filename'],
                title=kwargs['title'],
                description=kwargs['description'],
                author=kwargs['author'],
                version=kwargs['version'],
                show_date=kwargs['show_date'],
                show_glow=kwargs['show_glow'],
                show_border=kwargs['show_border'],
                border_color=kwargs['border_color'],
            )
        except Exception as e:
            put_error(f"❌ خطأ في التوليد: {e}")
            return

        # عرض
        put_html(f'''
        <div style="background:#e8e8e8;padding:20px;border-radius:12px;
            text-align:center;margin:15px 0;overflow:auto;">
            <div id="svgWrapper" style="display:inline-block;
                box-shadow:0 10px 30px rgba(0,0,0,0.25);border-radius:8px;
                overflow:hidden;">
                {svg_str}
            </div>
        </div>
        ''')

        info_parts = [f"📐 {w}×{h} px",
                     f"🎨 {kwargs['theme_name']}",
                     f"💻 {kwargs['lang_name']}"]
        if kwargs['title'].strip():
            info_parts.append(f"🏷️ {kwargs['title']}")
        if kwargs['description'].strip():
            info_parts.append("📝 يوجد شرح")
        if kwargs['show_glow']:
            info_parts.append("🌟 توهج")
        if kwargs['show_border']:
            info_parts.append("🔲 إطار")

        put_info(" | ".join(info_parts))

        # ═══ التحميل ═══
        put_markdown("### 💾 التحميل")

        base_name = kwargs['filename'].strip().rsplit(".", 1)[0] if kwargs['filename'].strip() else "code"
        if not base_name:
            base_name = "code"
        safe_name = "".join(c for c in base_name if c.isalnum() or c in "_-")
        theme_safe = "".join(c for c in kwargs['theme_name'] if c.isalnum() or c in "_-")

        # JavaScript للتحميل
        png_js = f'''
        (function() {{
            try {{
                var svg = document.querySelector('#svgWrapper svg');
                if (!svg) {{ alert('SVG غير موجود'); return; }}
                var svg_data = new XMLSerializer().serializeToString(svg);
                var svg_blob = new Blob([svg_data], {{type: 'image/svg+xml;charset=utf-8'}});
                var url = URL.createObjectURL(svg_blob);
                var img = new Image();
                img.onload = function() {{
                    var canvas = document.createElement('canvas');
                    canvas.width = {w} * 2;
                    canvas.height = {h} * 2;
                    var ctx = canvas.getContext('2d');
                    ctx.scale(2, 2);
                    ctx.drawImage(img, 0, 0);
                    canvas.toBlob(function(blob) {{
                        var dl = URL.createObjectURL(blob);
                        var a = document.createElement('a');
                        a.href = dl;
                        a.download = '{safe_name}_{theme_safe}.png';
                        document.body.appendChild(a);
                        a.click();
                        document.body.removeChild(a);
                        URL.revokeObjectURL(dl);
                    }}, 'image/png', 1.0);
                    URL.revokeObjectURL(url);
                }};
                img.onerror = function() {{
                    alert('فشل تحميل SVG');
                    URL.revokeObjectURL(url);
                }};
                img.src = url;
            }} catch(e) {{ alert('خطأ: ' + e.message); }}
        }})();
        '''

        jpg_js = f'''
        (function() {{
            try {{
                var svg = document.querySelector('#svgWrapper svg');
                if (!svg) {{ alert('SVG غير موجود'); return; }}
                var svg_data = new XMLSerializer().serializeToString(svg);
                var svg_blob = new Blob([svg_data], {{type: 'image/svg+xml;charset=utf-8'}});
                var url = URL.createObjectURL(svg_blob);
                var img = new Image();
                img.onload = function() {{
                    var canvas = document.createElement('canvas');
                    canvas.width = {w} * 2;
                    canvas.height = {h} * 2;
                    var ctx = canvas.getContext('2d');
                    ctx.fillStyle = '#ffffff';
                    ctx.fillRect(0, 0, canvas.width, canvas.height);
                    ctx.scale(2, 2);
                    ctx.drawImage(img, 0, 0);
                    canvas.toBlob(function(blob) {{
                        var dl = URL.createObjectURL(blob);
                        var a = document.createElement('a');
                        a.href = dl;
                        a.download = '{safe_name}_{theme_safe}.jpg';
                        document.body.appendChild(a);
                        a.click();
                        document.body.removeChild(a);
                        URL.revokeObjectURL(dl);
                    }}, 'image/jpeg', 0.95);
                    URL.revokeObjectURL(url);
                }};
                img.src = url;
            }} catch(e) {{ alert('خطأ: ' + e.message); }}
        }})();
        '''

        webp_js = f'''
        (function() {{
            try {{
                var svg = document.querySelector('#svgWrapper svg');
                if (!svg) {{ alert('SVG غير موجود'); return; }}
                var svg_data = new XMLSerializer().serializeToString(svg);
                var svg_blob = new Blob([svg_data], {{type: 'image/svg+xml;charset=utf-8'}});
                var url = URL.createObjectURL(svg_blob);
                var img = new Image();
                img.onload = function() {{
                    var canvas = document.createElement('canvas');
                    canvas.width = {w} * 2;
                    canvas.height = {h} * 2;
                    var ctx = canvas.getContext('2d');
                    ctx.scale(2, 2);
                    ctx.drawImage(img, 0, 0);
                    canvas.toBlob(function(blob) {{
                        var dl = URL.createObjectURL(blob);
                        var a = document.createElement('a');
                        a.href = dl;
                        a.download = '{safe_name}_{theme_safe}.webp';
                        document.body.appendChild(a);
                        a.click();
                        document.body.removeChild(a);
                        URL.revokeObjectURL(dl);
                    }}, 'image/webp', 0.95);
                    URL.revokeObjectURL(url);
                }};
                img.src = url;
            }} catch(e) {{ alert('خطأ: ' + e.message); }}
        }})();
        '''

        svg_js = f'''
        (function() {{
            try {{
                var svg = document.querySelector('#svgWrapper svg');
                if (!svg) {{ alert('SVG غير موجود'); return; }}
                var svg_data = new XMLSerializer().serializeToString(svg);
                var blob = new Blob([svg_data], {{type: 'image/svg+xml;charset=utf-8'}});
                var url = URL.createObjectURL(blob);
                var a = document.createElement('a');
                a.href = url;
                a.download = '{safe_name}_{theme_safe}.svg';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            }} catch(e) {{ alert('خطأ: ' + e.message); }}
        }})();
        '''

        print_js = '''
        window.print();
        '''

        put_buttons(
            ['📥 PNG', '📥 JPG', '📥 WebP', '📥 SVG', '🖨️ طباعة'],
            onclick=[
                lambda: run_js(png_js),
                lambda: run_js(jpg_js),
                lambda: run_js(webp_js),
                lambda: run_js(svg_js),
                lambda: run_js(print_js),
            ]
        )

        put_markdown("---")
        put_buttons(
            ['🔄 إعادة التوليد', '🎲 ثيم عشوائي'],
            onclick=[
                lambda: do_generate(**kwargs),
                lambda: random_theme_then_regenerate(**kwargs),
            ]
        )


def random_theme_then_regenerate(**kwargs):
    """توليد بثيم عشوائي"""
    themes = list(THEMES.keys())
    kwargs['theme_name'] = random.choice(themes)
    toast(f"🎲 تم اختيار: {kwargs['theme_name']}", color='success')
    do_generate(**kwargs)


# ═══════════════════════════════════════════════════════════
#                    🚀 التشغيل
# ═══════════════════════════════════════════════════════════

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    print(f"\n{'='*60}")
    print(f"  CodeCanvas Pro v{SITE_VERSION}")
    print(f"  Port: {port}")
    print(f"{'='*60}\n")
    start_server(main, port=port, host='0.0.0.0', debug=False)