import React from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';

interface CodeViewerProps {
  content: string;
  language: string;
}

export const CodeViewer: React.FC<CodeViewerProps> = ({ content, language }) => {
  return (
    <div className="code-viewer">
      <SyntaxHighlighter 
        language={language} 
        style={vscDarkPlus}
        customStyle={{
          margin: 0,
          background: 'transparent',
          fontSize: '0.9rem',
          lineHeight: '1.5'
        }}
        showLineNumbers={true}
      >
        {content}
      </SyntaxHighlighter>
    </div>
  );
};
