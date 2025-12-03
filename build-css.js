const { exec } = require("child_process");

console.log("🔄 Building Tailwind CSS...");
exec(
  "npx tailwindcss -i src/tailwind.css -o dist/output.css --minify",
  (error, stdout, stderr) => {
    if (error) {
      console.error("❌ Build failed:", error);
      return;
    }
    console.log("✅ Tailwind CSS built successfully!");
    console.log("📁 Output: dist/output.css");
  }
);
