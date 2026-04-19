import { useState, useEffect } from 'react'
import { fetchFiles, type FileNode } from './utils/fileTree'
import { Sidebar } from './components/Sidebar'
import { MarkdownViewer } from './components/MarkdownViewer'
import { CodeViewer } from './components/CodeViewer'
import { Hero } from './components/Hero'

function App() {
  const [tree, setTree] = useState<FileNode | null>(null)
  const [activePath, setActivePath] = useState<string>('')
  
  // Content states
  const [leftContent, setLeftContent] = useState<string>('')
  const [rightContent, setRightContent] = useState<string>('')
  const [rightLang, setRightLang] = useState<string>('python')
  const [leftLoading, setLeftLoading] = useState(false)
  const [rightLoading, setRightLoading] = useState(false)
  
  // Track current viewed files for titles
  const [leftTitle, setLeftTitle] = useState('')
  const [rightTitle, setRightTitle] = useState('')

  useEffect(() => {
    const fileTree = fetchFiles()
    setTree(fileTree)
  }, [])

  // Find siblings of a given path
  const findSiblings = (root: FileNode, targetPath: string): FileNode[] => {
    const parts = targetPath.replace('../notes/', '').split('/')
    const dirParts = parts.slice(0, -1)
    
    let currentNode = root
    for (const part of dirParts) {
      if (currentNode.children && currentNode.children[part]) {
        currentNode = currentNode.children[part]
      } else {
        return []
      }
    }
    
    return currentNode.children ? Object.values(currentNode.children).filter(n => n.type === 'file') : []
  }

  const getExt = (filename: string) => filename.split('.').pop() || ''
  const isMd = (ext: string) => ext === 'md'

  const handleSelectFile = async (node: FileNode) => {
    if (!node.path || !tree) return
    setActivePath(node.path)
    
    const ext = getExt(node.name)
    const siblings = findSiblings(tree, node.path)
    
    let mdNode: FileNode | undefined
    let codeNode: FileNode | undefined

    if (isMd(ext)) {
      mdNode = node
      // Find priority code node (we prefer the first non-md file)
      codeNode = siblings.find(s => !isMd(getExt(s.name)))
    } else {
      codeNode = node
      // Find priority md node (prefer description.md, else concept.md, else any .md)
      mdNode = siblings.find(s => s.name.toLowerCase() === 'description.md') 
              || siblings.find(s => s.name.toLowerCase() === 'concept.md')
              || siblings.find(s => isMd(getExt(s.name)))
    }

    // Unset contents instantly
    setLeftContent('')
    setRightContent('')
    setLeftTitle('')
    setRightTitle('')

    if (mdNode && mdNode.contentLoader) {
      setLeftLoading(true)
      try {
        const content = await mdNode.contentLoader()
        setLeftContent(content)
        setLeftTitle(mdNode.name)
      } finally {
        setLeftLoading(false)
      }
    }

    if (codeNode && codeNode.contentLoader) {
      setRightLoading(true)
      try {
        const content = await codeNode.contentLoader()
        setRightContent(content)
        setRightTitle(codeNode.name)
        
        const codeExt = getExt(codeNode.name)
        const langMap: Record<string, string> = {
          'py': 'python',
          'js': 'javascript',
          'ts': 'typescript',
          'java': 'java',
          'cpp': 'cpp',
          'c': 'c'
        }
        setRightLang(langMap[codeExt] || 'javascript')
      } finally {
        setRightLoading(false)
      }
    }
  }

  if (!tree) return <div className="loading">Loading Environment...</div>

  return (
    <div className="layout-container">
      <div className="sidebar-container">
        <Sidebar tree={tree} onSelectFile={handleSelectFile} activePath={activePath} />
      </div>
      
      <div className="panes-container">
        {!activePath ? (
          <Hero />
        ) : (
          <>
            { /* Left Pane (Documentation) */ }
            <div className={`pane left-pane ${!rightContent ? 'pane-centered' : ''}`}>
              <div className="pane-header">
                <span className="pane-title">{leftTitle || 'Documentation'}</span>
              </div>
              <div className="pane-content">
                {leftLoading ? (
                  <div className="loading">Fetching...</div>
                ) : leftContent ? (
                  <MarkdownViewer content={leftContent} />
                ) : (
                  <div className="empty-state">No documentation available for this view.</div>
                )}
              </div>
            </div>

            { /* Right Pane (Code) */ }
            {rightContent && (
              <div className="pane right-pane">
                <div className="pane-header">
                  <span className="pane-title">{rightTitle || 'Code'}</span>
                </div>
                <div className="pane-content code-pane-content">
                  {rightLoading ? (
                    <div className="loading">Fetching...</div>
                  ) : (
                    <CodeViewer content={rightContent} language={rightLang} />
                  )}
                </div>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  )
}

export default App
