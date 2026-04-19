export type FileNode = {
  name: string;
  path?: string;
  type: 'file' | 'directory';
  children?: Record<string, FileNode>;
  contentLoader?: () => Promise<string>;
};

export const fetchFiles = () => {
  // Grab all files strictly inside the notes directory!
  const modules = import.meta.glob('../notes/**/*.{md,py,java,cpp,c,js,ts}', { query: '?raw', import: 'default' });
  
  const root: FileNode = { name: 'notes', type: 'directory', children: {} };

  for (const path in modules) {
    // path looks like "../notes/Algorithms/Sorting/Bubble Sort/solution.py"
    // Remove "../notes/" to get a clean relative path
    const cleanPath = path.replace('../notes/', '');
    const parts = cleanPath.split('/');
    
    let currentNode = root;
    
    parts.forEach((part, index) => {
      if (!currentNode.children) {
        currentNode.children = {};
      }
      
      // If it's the last part, it's a file
      if (index === parts.length - 1) {
        currentNode.children[part] = {
          name: part,
          path: path, // keep the full original path for fetching later
          type: 'file',
          contentLoader: modules[path] as () => Promise<string>,
        };
      } else {
        // It's a directory
        if (!currentNode.children[part]) {
          currentNode.children[part] = {
            name: part,
            type: 'directory',
            children: {},
          };
        }
        currentNode = currentNode.children[part];
      }
    });
  }
  
  return root;
};
