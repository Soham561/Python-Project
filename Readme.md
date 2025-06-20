<h2 align="center">🚀 Part 1: <strong>Groq Chatbot Installation Process</strong></h2>

<hr/>

<ol>
  <li><strong>Create Project Folder</strong><br/>
  <code>mkdir Python-Project</code> <br/>
  <code>cd Python-Project</code>
  </li><br/>

  <li><strong>Create & Save <code>.env</code> file</strong><br/>
  Add your Groq API key inside it:<br/>
  <code>GROQ_API_KEY=your_groq_key_here</code><br/>
  <em>⚠️ Make sure to add <code>.env</code> to your <code>.gitignore</code> file!</em>
  </li><br/>

  <li><strong>Install Required Libraries</strong><br/>
  <code>pip install requests python-dotenv gradio</code>
  </li><br/>

  <li><strong>Create <code>chatbot.py</code> with Groq logic</strong><br/>
  This file will contain your API integration logic.
  </li><br/>

  <li><strong>Create <code>main.py</code> for Terminal CLI Chatbot</strong><br/>
  Use a loop to take input and respond using <code>chatbot.py</code>.
  </li><br/>

  <li><strong>(Optional) Add GUI Chatbot using Gradio</strong><br/>
  Launch a clean frontend using:<br/>
  <code>gr.ChatInterface(fn=ask_chatgpt, title="Groq Chatbot").launch()</code>
  </li>
</ol>

<hr/>

<p align="center"><strong>🎉 You're all set to run your chatbot via Terminal or Web UI!</strong></p>