const fs = require("fs"),
    path = require("path"),
    rootDir = path.resolve(__dirname, "..", "src"); // Always targets the root folder

function deleteClassFiles(dir) {
    if (!fs.existsSync(dir)) return;

    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
        const fullPath = path.join(dir, entry.name);
        if (entry.isDirectory()) deleteClassFiles(fullPath);
        else if (entry.isFile() && (entry.name.endsWith(".class") || entry.name.endsWith(".exe") || entry.name === "tempCodeRunnerFile.py")) {
            fs.unlinkSync(fullPath);
            console.log("🗑️  Deleted:", fullPath);
        }
    }
}

console.log("🧹 Cleaning .class, .exe, and tempCodeRunnerFile.py files...");
deleteClassFiles(rootDir);
console.log("✅ Done!");