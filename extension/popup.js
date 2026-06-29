document.addEventListener("DOMContentLoaded", () => {

    const askButton = document.getElementById("askButton");
    const response = document.getElementById("response");

    askButton.addEventListener("click", async () => {

        const question = document
            .getElementById("question")
            .value
            .trim();

        // Get the currently active tab
        const [tab] = await chrome.tabs.query({
            active: true,
            currentWindow: true
        });

        if (!question) {
            response.textContent = "Please enter a question.";
            return;

        }

        // Send a message to content.js
        chrome.tabs.sendMessage(
            tab.id,
            { action: "getPageContent" },
            async (pageData) => {

                if (chrome.runtime.lastError) {

                response.textContent =

                    "❌ This page cannot be analyzed.";

                console.error(
                    "Runtime Error:",
                    chrome.runtime.lastError.message
                );

                return;

            }

            if (!pageData) {

                response.textContent =

                    "❌ No page data received.";

                return;

            }

            // ================= DEBUG START =================

            console.log("========== PAGE DATA ==========");
            console.log(pageData);
            console.log("Title:", pageData.title);
            console.log("URL:", pageData.url);
            console.log("Question:", question);
            console.log("================================");

            // ================= DEBUG END =================

                response.textContent = "🤖 Thinking...";

                const backendResponse = await fetch(
                    "http://127.0.0.1:8000/ask",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type": "application/json"
                        },

                        body: JSON.stringify({
                            question: question,
                            page_title: pageData.title,
                            page_url: pageData.url,
                            page_text: pageData.text
                        })
                    }
                );

                const result = await backendResponse.json();

                response.textContent = result.answer;
            }
        );

    });

});



// document.addEventListener("DOMContentLoaded", () => {

//     const askButton = document.getElementById("askButton");
//     const response = document.getElementById("response");

//     askButton.addEventListener("click", async () => {

//         response.textContent = "🤖 Reading webpage...";

//         const [tab] = await chrome.tabs.query({
//             active: true,
//             currentWindow: true
//         });

//         chrome.tabs.sendMessage(
//             tab.id,
//             { action: "getPageContent" },
//             (pageData) => {

//                 console.log("========== PAGE DATA ==========");
//                 console.log(pageData);
//                 console.log("===============================");

//                 if (chrome.runtime.lastError) {
//                     console.error(chrome.runtime.lastError);

//                     response.textContent =
//                         "❌ " + chrome.runtime.lastError.message;

//                     return;
//                 }

//                 if (!pageData) {
//                     response.textContent =
//                         "❌ No page data received.";

//                     return;
//                 }

//                 console.log("Title:", pageData.title);
//                 console.log("URL:", pageData.url);

//                 console.log("First 500 characters:");
//                 console.log(pageData.text.substring(0, 500));

//                 response.textContent =
//                     "✅ Page read successfully!\n\n" +
//                     pageData.title;

//             }
//         );

//     });

// });