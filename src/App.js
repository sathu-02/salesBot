// import React, { useState, useRef, useEffect } from "react";
// import ReactMarkdown from "react-markdown";

// import { BrowserRouter as Router, Routes, Route, useNavigate } from "react-router-dom";
// import "./App.css";
// import Particles from "../src/components/Particles.jsx";
// import Login from "./components/Login.js";
// import Signup from "./components/Signup.js";

// function Chat() {
//   const [messages, setMessages] = useState([
//     { text: "Hi, How may I Help You?..", sender: "bot" }
//   ]);
//   const [input, setInput] = useState("");
//   const messagesEndRef = useRef(null);
//   const navigate = useNavigate();

//   useEffect(() => {
//     messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
//   }, [messages]);

//   const sendMessage = async () => {
//     if (input.trim() === "") return;

//     const userMessage = { text: input, sender: "user" };
//     const typeBotResponse = (text) => {
//       let index = 0;
//       const speed = 15; // Typing speed in ms

//       const interval = setInterval(() => {
//         setMessages((prevMessages) => {
//           const last = prevMessages[prevMessages.length - 1];
//           const updated = { ...last, text: text.slice(0, index) };
//           return [...prevMessages.slice(0, -1), updated];
//         });

//         index++;
//         if (index > text.length) clearInterval(interval);
//       }, speed);
//     };

//     setInput("");

//     try {
//       const res = await fetch("http://localhost:5000/chat", {
//         method: "POST",
//         headers: {
//           "Content-Type": "application/json",
//         },
//         body: JSON.stringify({
//           query: input,
//           forecast_month: new Date().toLocaleString("default", {
//             month: "long",
//             year: "numeric",
//           }), // optional
//         }),
//       });

//       const data = await res.json();
//       setMessages((prev) => [...prev, { text: "", sender: "bot" }]); // Placeholder message

//       if (data.response) {
//         typeBotResponse(data.response);
//       }


//       if (data.response) {
//         setMessages((prev) => [
//           ...prev,
//           { text: data.response, sender: "bot" },
//         ]);
//       } else if (data.forecast) {
//         const forecastSummary = data.forecast
//           .map(
//             (f) =>
//               `${f.customername} - ${f.itemname}: 💲${f.forecasted_amt_usd}, 📦 ${f.forecasted_units} ${f.Unit_Name}`
//           )
//           .join("\n");

//         setMessages((prev) => [
//           ...prev,
//           { text: "📊 Forecast:\n" + forecastSummary, sender: "bot" },
//         ]);
//       } else if (data.error) {
//         setMessages((prev) => [
//           ...prev,
//           { text: `⚠️ Error: ${data.error}`, sender: "bot" },
//         ]);
//       }
//     } catch (error) {
//       setMessages((prev) => [
//         ...prev,
//         { text: `❌ Failed to fetch: ${error.message}`, sender: "bot" },
//       ]);
//     }
//   };


//   const handleKeyDown = (e) => {
//     if (e.key === "Enter") sendMessage();
//   };

//   const handleCopy = (text) => {
//     navigator.clipboard.writeText(text);
//   };

//   const handleSpeak = (text) => {
//     if ('speechSynthesis' in window) {
//       const utter = new window.SpeechSynthesisUtterance(text);
//       window.speechSynthesis.speak(utter);
//     }
//   };

//   return (
//     <div className="chat-bg">
//       <Particles />
//       <div className="chat-container">
//         <div className="header">
//           <h1 className="title">Knoxx</h1>
//           <div className="auth-buttons">
//           </div>
//         </div>
//         <div className="messages">
//          {messages.map((msg, idx) => (
//   <div key={idx} className={`message-wrapper ${msg.sender}`}>
//     <div className={`message-bubble ${msg.sender}`}>
//       {msg.sender === "bot" ? (
//         <ReactMarkdown className="message-markdown">
//           {msg.text}
//         </ReactMarkdown>
//       ) : (
//         msg.text
//       )}
//     </div>
//   </div>
// ))}

//               {msg.sender === "bot" && (
//                 <div className="bot-actions">
//                   <button
//                     className="icon-btn"
//                     title="Copy"
//                     onClick={() => handleCopy(msg.text)}
//                   >
//                     <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
//                       <rect x="5" y="5" width="10" height="12" rx="2" stroke="#fff" strokeWidth="2" fill="none"/>
//                       <rect x="3" y="3" width="10" height="12" rx="2" stroke="#fff" strokeWidth="1" fill="none" opacity="0.5"/>
//                     </svg>
//                   </button>
//                   <button
//                     className="icon-btn"
//                     title="Speak"
//                     onClick={() => handleSpeak(msg.text)}
//                   >
//                     <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
//                       <path d="M3 8v4h4l5 5V3l-5 5H3z" fill="#fff"/>
//                       <path d="M15.54 8.46a5 5 0 010 7.07" stroke="#fff" strokeWidth="1.5" fill="none"/>
//                       <path d="M17.66 6.34a8 8 0 010 11.32" stroke="#fff" strokeWidth="1" fill="none"/>
//                     </svg>
//                   </button>
//                 </div>
//               )}
//             </div>
//           ))}
//           <div ref={messagesEndRef} />
//         </div>
//         <div className="input-area">
//           <input
//             type="text"
//             placeholder="Type your message..."
//             value={input}
//             onChange={(e) => setInput(e.target.value)}
//             onKeyDown={handleKeyDown}
//           />
//           <button className="mic-btn" title="Voice input (coming soon)">
//             <img src="/mic.svg" alt="Mic" style={{ width: 24, height: 24 }} />
//           </button>
//           <button onClick={sendMessage}>Send</button>
//         </div>
//       </div>
//     </div>
//   );
// }

// function App() {
//   return (
//     <Router>
//       <Routes>
//         <Route path="/" element={<Chat />} />
//         <Route path="/login" element={<Login navigateTo={path => window.location.href = path} />} />
//         <Route path="/signup" element={<Signup navigateTo={path => window.location.href = path} />} />
//       </Routes>
//     </Router>
//   );
// }

// export default App;



import React, { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate,
} from "react-router-dom";

import "./App.css";
import Particles from "./components/Particles.jsx";
import Login from "./components/Login.js";
import Signup from "./components/Signup.js";

function Chat() {
  const [messages, setMessages] = useState([
    { text: "Hi, How may I Help You?..", sender: "bot" },
  ]);
  const [input, setInput] = useState("");
  const messagesEndRef = useRef(null);
  const navigate = useNavigate();

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (input.trim() === "") return;

    const userMessage = { text: input, sender: "user" };
    setMessages((prev) => [...prev, userMessage, { text: "", sender: "bot" }]);
    setInput("");

    const typeBotResponse = (text) => {
      let index = 0;
      const speed = 10;
      const interval = setInterval(() => {
        setMessages((prevMessages) => {
          const updated = [...prevMessages];
          const last = updated[updated.length - 1];
          updated[updated.length - 1] = {
            ...last,
            text: text.slice(0, index),
          };
          return updated;
        });
        index++;
        if (index > text.length) clearInterval(interval);
      }, speed);
    };

    try {
      const forecastMonth = new Date(
        new Date().getFullYear(),
        new Date().getMonth() + 1
      ).toLocaleString("default", {
        month: "long",
        year: "numeric",
      });

      const res = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          query: input,
          forecast_month: forecastMonth,
        }),
      });

      const data = await res.json();

      const botMessage = {
        text: data.response || "🤖 Sorry, no response received.",
        sender: "bot",
        ...(data.streamlit_url && {
          streamlitUrl: data.streamlit_url,
          downloadUrl: "/static/forecast_results.csv",
        }),
      };


      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1] = botMessage;
        return updated;
      });
    } catch (error) {
      typeBotResponse(`❌ Failed to fetch: ${error.message}`);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  const handleCopy = (text) => {
    navigator.clipboard.writeText(text);
  };

  const handleSpeak = (text) => {
    if ("speechSynthesis" in window) {
      const utter = new window.SpeechSynthesisUtterance(text);
      window.speechSynthesis.speak(utter);
    }
  };

  const handleListen = () => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Speech recognition not supported in this browser.");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.start();

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setInput(transcript);
    };

    recognition.onerror = (event) => {
      console.error("Speech recognition error:", event.error);
    };
  };

  return (
    <div className="chat-bg">
      <Particles />
      <div className="chat-container">
        <div className="header">
          <nav className="navbar">
            <h1
              style={{
                color: "#FF0000",
                fontFamily: "'Orbitron', sans-serif",
                fontSize: "3rem",
                letterSpacing: "3px",
              }}
            >
              Sales Bot
            </h1>
          </nav>
        </div>

        <div className="messages">
          {messages.map((msg, idx) => (
            <div key={idx} className={`message-wrapper ${msg.sender}`}>
              <div className={`message-bubble ${msg.sender}`}>
                {msg.sender === "bot" ? (
                  <div className="bot-message">
                    <ReactMarkdown>{msg.text}</ReactMarkdown>

                    {/* ✅ STREAMLIT LINK */}
                    {msg.streamlitUrl && (
                      <a
                        href={msg.streamlitUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        style={{
                          display: "inline-block",
                          marginTop: "10px",
                          padding: "6px 12px",
                          backgroundColor: "#28a745",
                          color: "white",
                          borderRadius: "5px",
                          textDecoration: "none",
                        }}
                      >
                        📈 View/Download Forecast
                      </a>
                    )}

                    {/* ✅ DIRECT CSV DOWNLOAD LINK */}
                    
                  </div>
                ) : (
                  msg.text
                )}
              </div>

              {msg.sender === "bot" && msg.text && (
                <div className="bot-actions">
                  <button
                    className="icon-btn"
                    title="Copy"
                    onClick={() => handleCopy(msg.text)}
                  >
                    📋
                  </button>
                  <button
                    className="icon-btn"
                    title="Speak"
                    onClick={() => handleSpeak(msg.text)}
                  >
                    🔊
                  </button>
                </div>
              )}
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>

        <div className="input-area">
          <input
            type="text"
            placeholder="Type your message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
          />
          <button
            className="mic-btn"
            title="Voice input"
            onClick={handleListen}
          >
            <img src="/mic.svg" alt="Mic" style={{ width: 24, height: 24 }} />
          </button>
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Chat />} />
        <Route
          path="/login"
          element={
            <Login navigateTo={(path) => (window.location.href = path)} />
          }
        />
        <Route
          path="/signup"
          element={
            <Signup navigateTo={(path) => (window.location.href = path)} />
          }
        />
      </Routes>
    </Router>
  );
}

export default App;



