const fs = require("fs"),
    path = require("path"),
    rootDir = path.join(process.cwd(), "src"),
    QUERY = process.argv[2]?.toLowerCase(); // For handling user input

function findDirectory(dir, target) { // Recursively search for a directory matching the query
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
        if (entry.isDirectory()) {
            if (entry.name.toLowerCase() === target) return path.join(dir, entry.name);
            const found = findDirectory(path.join(dir, entry.name), target);
            if (found) return found; // Stop at first match
        }
    }
    return null; // No match found
}

function printTree(dir, prefix = "") {
    let entries;
    try { // Read directory contents with type info
        entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch { // Handle inaccessible directories gracefully
        console.error(prefix + "└── [Cannot access directory]");
        return;
    }

    entries.forEach((entry, index) => {
        const isLast = index === entries.length - 1,
            connector = isLast ? "└── " : "├── ", // Tree formatting
            fullPath = path.join(dir, entry.name);

        console.log(prefix + connector + entry.name); // Print current file/folder

        if (entry.isDirectory()) { // If directory, recursively print its contents
            const extension = isLast ? "    " : "│   ";
            printTree(fullPath, prefix + extension);
        }
    });
}

function main() {
    if (!fs.existsSync(rootDir) || !fs.statSync(rootDir).isDirectory()) { // Validate root directory exists
        console.error("❌ src directory not found.");
        process.exit(1);
    }
    if (!QUERY) { // No query → print full tree
        console.log("src");
        printTree(rootDir);
        return;
    }
    const targetDir = findDirectory(rootDir, QUERY);
    if (!targetDir) {
        console.log(`❌ "${QUERY}" not found`);
        return;
    }
    console.log(path.basename(targetDir)); // Print only the matched directory tree
    printTree(targetDir);
}

main();