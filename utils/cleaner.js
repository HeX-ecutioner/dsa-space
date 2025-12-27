#!/usr/bin/env node

const fs = require("fs"),
    path = require("path"),
    rootDir = path.resolve(__dirname, "..", "src"); // Always target the root folder

function deleteClassFiles(dir) {
    if (!fs.existsSync(dir)) return;

    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
        const fullPath = path.join(dir, entry.name);
        if (entry.isDirectory()) deleteClassFiles(fullPath);
        else if (entry.isFile() && (entry.name.endsWith(".class") || entry.name.endsWith(".exe"))) {
            fs.unlinkSync(fullPath);
            console.log("🗑️  Deleted:", fullPath);
        }
    }
}

console.log("🧹 Cleaning .class and .exe files...");
deleteClassFiles(rootDir);
console.log("✅ Done!");