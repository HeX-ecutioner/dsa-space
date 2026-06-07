import { useState, useEffect } from 'react'
import { fetchFiles, type FileNode } from './utils/fileTree'
import { Sidebar } from './components/Sidebar'
import { MarkdownViewer } from './components/MarkdownViewer'
import { CodeViewer } from './components/CodeViewer'
import { Hero } from './components/Hero'

const ext = (f: string) => f.split('.').pop() || '';
const isMd = (e: string) => e === 'md';
const langs: Record<string, string> = { py: 'python', js: 'javascript', ts: 'typescript', java: 'java', cpp: 'cpp', c: 'c' };

function App() {
  const [tree, setTree] = useState<FileNode | null>(null)
  const [activePath, setActivePath] = useState('')
  const [p, setP] = useState({ l: '', r: '', lLd: false, rLd: false, lT: '', rT: '', rL: 'python' })
  const [m, setM] = useState({ side: false, tab: 'doc' as 'doc'|'code' })

  useEffect(() => setTree(fetchFiles()), [])

  const handleSelectFile = async (node: FileNode) => {
    if (!node.path || !tree) return
    setActivePath(node.path)
    const e = ext(node.name)
    setM({ side: false, tab: isMd(e) ? 'doc' : 'code' })

    const parts = node.path.replace('../notes/', '').split('/').slice(0, -1)
    let curr = tree
    for (const part of parts) curr = curr.children?.[part] || curr
    const sibs = curr.children ? Object.values(curr.children).filter(n => n.type === 'file') : []

    let mdNode = isMd(e) ? node : sibs.find(s => ['description.md', 'concept.md'].includes(s.name.toLowerCase()) || isMd(ext(s.name)))
    let cdNode = isMd(e) ? sibs.find(s => !isMd(ext(s.name))) : node

    setP(prev => ({ ...prev, l: '', r: '', lT: '', rT: '', lLd: !!mdNode, rLd: !!cdNode }))

    if (mdNode?.contentLoader) {
      const c = await mdNode.contentLoader()
      setP(prev => ({ ...prev, l: c, lT: mdNode!.name, lLd: false }))
    }
    if (cdNode?.contentLoader) {
      const c = await cdNode.contentLoader()
      setP(prev => ({ ...prev, r: c, rT: cdNode!.name, rL: langs[ext(cdNode!.name)] || 'javascript', rLd: false }))
    }
  }

  const getTitle = () => {
    if (!activePath) return 'DSA Space'
    const parts = activePath.replace('../notes/', '').split('/')
    return parts.length > 1 ? parts[parts.length - 2] : parts[0]
  }

  if (!tree) return <div className="loading">Loading Environment...</div>

  return (
    <div className={`layout-container ${m.side ? 'sidebar-open' : ''}`}>
      <div className="mobile-header">
        <button className="mobile-sidebar-toggle" onClick={() => setM(x => ({ ...x, side: !x.side }))}>{m.side ? '✕' : '☰'}</button>
        <span className="mobile-header-title">{getTitle()}</span>
        <div style={{ width: 24 }}></div>
      </div>

      {m.side && <div className="sidebar-overlay" onClick={() => setM(x => ({ ...x, side: false }))} />}

      <div className="sidebar-container">
        <Sidebar tree={tree} onSelectFile={handleSelectFile} activePath={activePath} />
      </div>
      
      <div className="panes-container">
        {activePath && (p.l || p.lLd) && p.r && (
          <div className="mobile-tabs-container">
            <button className={`mobile-tab-btn ${m.tab === 'doc' ? 'active' : ''}`} onClick={() => setM(x => ({ ...x, tab: 'doc' }))}>📖 Doc</button>
            <button className={`mobile-tab-btn ${m.tab === 'code' ? 'active' : ''}`} onClick={() => setM(x => ({ ...x, tab: 'code' }))}>💻 Code</button>
          </div>
        )}

        {!activePath ? <Hero /> : (
          <>
            {(p.l || p.lLd) && (
              <div className={`pane left-pane ${!p.r ? 'pane-centered' : ''} ${m.tab === 'doc' ? 'mobile-active' : ''}`}>
                <div className="pane-header"><span className="pane-title">{p.lT || 'Documentation'}</span></div>
                <div className="pane-content">{p.lLd ? <div className="loading">Fetching...</div> : <MarkdownViewer content={p.l} />}</div>
              </div>
            )}
            {p.r && (
              <div className={`pane right-pane ${!(p.l || p.lLd) ? 'pane-centered' : ''} ${m.tab === 'code' ? 'mobile-active' : ''}`}>
                <div className="pane-header"><span className="pane-title">{p.rT || 'Code'}</span></div>
                <div className="pane-content code-pane-content">{p.rLd ? <div className="loading">Fetching...</div> : <CodeViewer content={p.r} language={p.rL} />}</div>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  )
}

export default App
