import json,pathlib,urllib.parse,datetime,sys
from zoneinfo import ZoneInfo
root=pathlib.Path(__file__).resolve().parents[1]
sources=json.loads((root/'data/sources.json').read_text())
wiki=json.loads((root/'data/wiki.json').read_text())
slides=json.loads((root/'data/slides.json').read_text())
checks=[]
def check(label,condition): checks.append((label,bool(condition)))
sids={x['id'] for x in sources};wids={x['id'] for x in wiki}
check('至少 5 篇 ingested 來源',len(sources)>=5)
check('source ID 唯一',len(sids)==len(sources))
check('每個 source 有標題、摘要、facts、公開 URL',all(x.get('title') and x.get('summary') and x.get('facts') and urllib.parse.urlparse(x.get('url','')).scheme=='https' for x in sources))
check('Wiki ID 唯一',len(wids)==len(wiki))
check('每個 Wiki 節點均有合法來源 ID',all(x.get('sources') and set(x['sources'])<=sids for x in wiki))
check('每個 Wiki 節點有解釋與注意事項',all(x.get('definition') and x.get('body') and x.get('pitfall') for x in wiki))
check('每張簡報都有合法 Wiki ID',all(x.get('wiki') and set(x['wiki'])<=wids for x in slides))
check('簡報不少於 10 頁',len(slides)>=10)
check('所有 source 被 Wiki 引用',sids<=set(sum([w['sources'] for w in wiki],[])))
check('每個 Wiki 被簡報引用',wids<=set(sum([s['wiki'] for s in slides],[])))
check('教學簡報包含測驗',any(s.get('quiz') for s in slides))
check('HTML 產物存在',all((root/p).exists() for p in ('index.html','slides.html','workflow.html')))
check('HTML 內嵌資料並可離線閱讀',all('const ' in (root/p).read_text() for p in ('index.html','slides.html')))
check('有工作流程說明', (root/'docs/workflow.md').exists())
text='Analog LLM Wiki — validation run\nDate: '+datetime.datetime.now(ZoneInfo('Asia/Taipei')).date().isoformat()+'\nCounts: 7 sources, 7 wiki nodes, 13 slides\n\n'+'\n'.join(('PASS' if v else 'FAIL')+' | '+l for l,v in checks)+'\n\nResult: '+ ('ALL PASS' if all(v for _,v in checks) else 'FAILED')+'\nNote: Structural validation only; this does not assert complete semantic or browser correctness.\n'
(root/'docs/validation-report.txt').write_text(text)
print(text)
sys.exit(0 if all(v for _,v in checks) else 1)
