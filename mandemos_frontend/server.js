const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve static files relative to this script's directory so the
// server works even when launched from another path
app.use(express.static(path.join(__dirname, 'public')));
// Explicit route for the chat UI to keep the old chat.html path working
app.get('/chat.html', (req, res) => {
  res.sendFile(path.resolve(__dirname, 'public', 'chat_ui.html'));
});
app.get('*', (req, res) => {
  res.sendFile(path.resolve(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`MandemOS Clone running on http://localhost:${PORT}`);
});
