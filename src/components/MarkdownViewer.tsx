import React from 'react';
import Markdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

interface MarkdownViewerProps {
  content: string;
}

export const MarkdownViewer: React.FC<MarkdownViewerProps> = ({ content }) => {
  return (
    <div className="markdown-viewer">
      <Markdown remarkPlugins={[remarkGfm]}>
        {content}
      </Markdown>
    </div>
  );
};
