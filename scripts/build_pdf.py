#!/usr/bin/env python3
"""Build the print-ready brief from the public editorial content and Figma exports."""
import json
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle, KeepTogether
from reportlab.lib.utils import ImageReader

ROOT=Path(__file__).resolve().parents[1]
NAVY=colors.HexColor('#102B3D'); TEAL=colors.HexColor('#16776E'); INK=colors.HexColor('#253F50'); MUTED=colors.HexColor('#536777')
W,H=A4; CW=W-88
styles={
 'kicker':ParagraphStyle('kicker',fontName='Helvetica-Bold',fontSize=9,leading=13,textColor=TEAL,spaceAfter=10),
 'title':ParagraphStyle('title',fontName='Helvetica-Bold',fontSize=26,leading=30,textColor=NAVY,spaceAfter=15),
 'deck':ParagraphStyle('deck',fontName='Helvetica',fontSize=13,leading=19,textColor=MUTED,spaceAfter=17),
 'h':ParagraphStyle('h',fontName='Helvetica-Bold',fontSize=11,leading=16,textColor=NAVY,spaceBefore=13,spaceAfter=7),
 'body':ParagraphStyle('body',fontName='Helvetica',fontSize=10,leading=14.5,textColor=INK,spaceAfter=9),
 'small':ParagraphStyle('small',fontName='Helvetica',fontSize=8,leading=11,textColor=MUTED,spaceAfter=8),
}
def clean(s):
 return s.replace('→',' / ').replace('—',' - ').replace('–','-').replace('×','x').replace('‑','-')
def p(s,kind='body'): return Paragraph(escape(clean(s)),styles[kind])
def img(path,maxw,maxh):
 w,h=ImageReader(str(path)).getSize(); scale=min(maxw/w,maxh/h)
 return Image(str(path),width=w*scale,height=h*scale,hAlign='CENTER')
def footer(c,doc):
 c.saveState();c.setStrokeColor(colors.HexColor('#D8E1E7'));c.line(44,39,W-44,39)
 c.setFont('Helvetica',8);c.setFillColor(MUTED);c.drawString(44,26,'MAZE MEDIA  /  DESIGN & HOME-LAB PORTFOLIO');c.drawRightString(W-44,26,f'06 SEP 2026   /   {doc.page:02d}');c.restoreState()
content=json.loads((ROOT/'publication/content.json').read_text());story=[]
story += [img(ROOT/'assets/figma/cover.png',CW,330),Spacer(1,28),p('DESIGN BRIEF / PUBLIC EDITION','kicker'),p('A coherent experience for a privately operated collection.','title'),p('Product direction, four platform editions, service responsibilities and the path to verified delivery.','deck'),p('This brief accompanies the public MazeMedia repository. It summarizes the existing application design and its next steps. It does not publish binaries, operational credentials or a completed TestFlight release.'),p('Documentation checkpoint: September 6, 2026. Development build 11; build 9 remains the last recorded TestFlight release.','small'),Paragraph('<link href="https://github.com/Morlock52/MazeMedia" color="#16776E">github.com/Morlock52/MazeMedia</link>',styles['body']),PageBreak()]
story += [p('THE APPLICATION PORTFOLIO','kicker'),p('Four editions. One content model.','title'),img(ROOT/'assets/figma/platforms.png',CW,365),Spacer(1,14),p('The original screenshots use demo content. They show the implemented layout while protecting the owner’s library. Figma provides the editable publication structure around the captures.','small'),p('Reading this brief','h'),p('Pages 3-14 follow the twelve section folders in the repository. Each section has a design narrative and a separate PLAN.md. Proposed work and acceptance requirements are kept distinct from recorded results.'),p('Public scope','h'),p('The architecture preserves service roles and trust boundaries. The private baseline, IP inventory, management endpoints and personal household state are intentionally outside this public edition.'),PageBreak()]
for i,d in enumerate(content,1):
 story += [p(f'{i:02d} / SECTION PLAN','kicker'),p(d['title'],'title'),p(d['summary'],'deck')]
 if d['images']:
  left=[p(d['body']),p('User journey','h'),p(d['journey'])]
  right=[img(ROOT/'assets/screenshots'/d['images'][0],214,342),Spacer(1,8),p('Mac runtime / demo fixture, September 6.' if d['slug']=='05-mac' else 'Simulator / demo fixture, September 5.','small')]
  table=Table([[left,right]],colWidths=[CW-234,234]);table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(0,0),16),('RIGHTPADDING',(1,0),(1,0),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]));story.append(table)
 else:
  story += [p(d['body']),p('User journey','h'),p(d['journey'])]
 if d['slug']=='10-home-lab': story.append(img(ROOT/'assets/figma/architecture.png',CW,190))
 story.append(p('Next delivery priorities','h'))
 for n,s in enumerate(d['steps'],1): story.append(p(f'{n}. {s}'))
 story += [p('Required acceptance criteria','h'),p(' '.join(d['accept'])),p('Detailed decisions and requirements: sections/'+d['slug']+'/PLAN.md','small'),PageBreak()]
story += [p('EVIDENCE & REFERENCES','kicker'),p('A clear line between a design and a release.','title'),p('Recorded checks','h'),p('iPhone build 11 controls passed twice. The Mac recorded 70 unit tests passed and two opt-in skips, plus direct mouse checks. The final automated Mac mouse run was interrupted by a floating dialog. iPad and Apple TV controls acceptance, final archive refresh and Apple processing remain separate release gates.'),p('Home-lab proof','h'),p('Mealie and Home Assistant opened real content on iPhone and iPad with NetBird off over Wi-Fi. That does not establish cellular-only access, off-network initial enrollment, long-duration renewal or public access for other services.'),p('Source records','h'),p('Implementation revision: a0ea5e7b2048dc8fe97b43c83f29c64af0fc00a1. Network baseline: September 4, retrieved September 5, supplemented by later implementation entries. The repository evidence register names the retained test artifacts and distinguishes historical checkpoints.'),p('Continue in the repository','h')]
for name,url in [('Portfolio and section plans','https://github.com/Morlock52/MazeMedia'),('Editable Figma publication','https://www.figma.com/design/sfpDlUVIM1j8i4wZ1wjCBC'),('Primary upstream sources','https://github.com/Morlock52/MazeMedia/blob/main/REFERENCES.md')]:
 story.append(Paragraph(f'<link href="{url}" color="#16776E">{name}</link>',styles['body']))
story += [p('Publication and rights','h'),p('Screenshots remain real application captures. The Figma boards are editorial artwork. No open-source license is granted by this design publication; third-party service names remain the property of their respective projects.','small')]
out=ROOT/'publication/Maze-Media-Design-Brief.pdf'
SimpleDocTemplate(str(out),pagesize=A4,rightMargin=44,leftMargin=44,topMargin=44,bottomMargin=55,title='Maze Media - Design & Home-Lab Portfolio',author='Morlock52',subject='Platform editions, integration architecture and section plans').build(story,onFirstPage=footer,onLaterPages=footer)
print(out)
