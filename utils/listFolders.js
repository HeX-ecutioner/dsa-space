const fs = require("fs"),
    path = require("path"),
    SRC_DIR = path.join(process.cwd(), "src");

function listFolders(dir, prefix = "") {
    let entries;
    try {
        entries = fs.readdirSync(dir, { withFileTypes: true });
    } catch (err) {
        console.error(prefix + "└── [Cannot access directory]");
        return;
    }
    entries.sort((a, b) => a.name.localeCompare(b.name));
    entries.forEach((entry, index) => {
        const isLast = index === entries.length - 1,
            connector = isLast ? "└── " : "├── ",
            fullPath = path.join(dir, entry.name);
        console.log(prefix + connector + entry.name);
        if (entry.isDirectory()) {
            const extension = isLast ? "    " : "│   ";
            listFolders(fullPath, prefix + extension);
        }
    });
}

function main() {
    if (!fs.existsSync(SRC_DIR) || !fs.statSync(SRC_DIR).isDirectory()) {
        console.error("❌ src directory not found in current working directory.");
        process.exit(1);
    }

    console.log("src");
    listFolders(SRC_DIR);
}

main();