import React, { useState } from 'react';
import type { FileNode } from '../utils/fileTree';

interface SidebarProps {
  tree: FileNode;
  onSelectFile: (node: FileNode) => void;
  activePath?: string;
}

const TreeNode: React.FC<{
  node: FileNode;
  onSelectFile: (node: FileNode) => void;
  activePath?: string;
  defaultExpanded?: boolean;
}> = ({ node, onSelectFile, activePath, defaultExpanded = false }) => {
  const [isExpanded, setIsExpanded] = useState(defaultExpanded);

  if (node.type === 'file') {
    const isActive = activePath === node.path;
    return (
      <div 
        className={`tree-file ${isActive ? 'active' : ''}`}
        onClick={() => onSelectFile(node)}
      >
        <span className="file-icon">📄</span>
        <span className="file-name">{node.name}</span>
      </div>
    );
  }

  // It's a directory
  const children = node.children ? Object.values(node.children) : [];
  
  // Sort children: directories first, then files, alphabetically
  children.sort((a, b) => {
    if (a.type === b.type) {
      return a.name.localeCompare(b.name);
    }
    return a.type === 'directory' ? -1 : 1;
  });

  return (
    <div className="tree-directory">
      <div 
        className="directory-header"
        onClick={() => setIsExpanded(!isExpanded)}
      >
        <span className={`folder-icon ${isExpanded ? 'open' : ''}`}>
          {isExpanded ? '📂' : '📁'}
        </span>
        <span className="folder-name">{node.name}</span>
      </div>
      
      {isExpanded && (
        <div className="directory-children">
          {children.map(child => (
            <TreeNode 
              key={child.name} 
              node={child} 
              onSelectFile={onSelectFile} 
              activePath={activePath}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export const Sidebar: React.FC<SidebarProps> = ({ tree, onSelectFile, activePath }) => {
  // tree is the root "notes" node. 
  const rootChildren = tree.children ? Object.values(tree.children) : [];
  
  rootChildren.sort((a, b) => {
    if (a.type === b.type) return a.name.localeCompare(b.name);
    return a.type === 'directory' ? -1 : 1;
  });

  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h2 className="title">DSA Notes</h2>
      </div>
      <div className="sidebar-content">
        {rootChildren.map(child => (
          <TreeNode 
            key={child.name} 
            node={child} 
            onSelectFile={onSelectFile} 
            activePath={activePath} 
            defaultExpanded={false}
          />
        ))}
      </div>
    </div>
  );
};
