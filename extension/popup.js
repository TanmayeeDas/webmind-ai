// document.addEventListener("DOMContentLoaded", () => {

//     const askButton = document.getElementById("askButton");
//     const response = document.getElementById("response");
//     let pageData=null;

//     // Automatically index the current page

//     const [tab] = await chrome.tabs.query({
//         active: true,
//         currentWindow: true
//     });

//     chrome.tabs.sendMessage(
//         tab.id,
//         { action: "getPageContent" },
//         async (data) => {

//             if (chrome.runtime.lastError || !data) {

//                 response.textContent =
//                     "❌ This page cannot be analyzed.";

//                 return;
//             }

//             pageData = data;

//             response.textContent = "📄 Indexing page...";

//             const backendResponse = await fetch(
//                 "http://127.0.0.1:8000/index-page",
//                 {

//                     method: "POST",

//                     headers: {
//                         "Content-Type": "application/json"
//                     },

//                     body: JSON.stringify({

//                         page_title: pageData.title,
//                         page_url: pageData.url,
//                         page_text: pageData.text

//                     })

//                 }
//             );

//             const result = await backendResponse.json();

//             response.textContent =
//                 `✅ ${result.message}

//     Total Chunks: ${result.chunks}`;

//         }
//     );
    
//     askButton.addEventListener("click", async () => {

//         const question = document
//             .getElementById("question")
//             .value
//             .trim();

//         if (!question) {
//             response.textContent = "Please enter a question.";
//             return;
//         }

//         response.textContent = "🔍 Retrieving context...";

//         const backendResponse = await fetch(
//             "http://127.0.0.1:8000/retrieve",
//             {
//                 method: "POST",

//                 headers: {
//                     "Content-Type": "application/json"
//                 },

//                 body: JSON.stringify({

//                     question: question

//                 })

//             }
//         );

//         const result = await backendResponse.json();

//         response.textContent =
//     `${result.message}

//     Retrieved Chunks: ${result.retrieved_chunks}`;

//     });

//     });




document.addEventListener("DOMContentLoaded", async () => {

    const askButton = document.getElementById("askButton");
    const response = document.getElementById("response");

    let pageData = null;
    let isIndexed = false;

    // -------------------------------
    // Automatically index current page
    // -------------------------------

    const [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true
    });

    chrome.tabs.sendMessage(
        tab.id,
        { action: "getPageContent" },
        async (data) => {

            if (chrome.runtime.lastError) {

                response.textContent =
                    "❌ This page cannot be analyzed.";

                console.error(chrome.runtime.lastError.message);

                return;
            }

            if (!data) {

                response.textContent =
                    "❌ No page data received.";

                return;
            }

            pageData = data;

            response.textContent = "📄 Indexing page...";

            try {

                const backendResponse = await fetch(
                    "http://127.0.0.1:8000/index-page",
                    {

                        method: "POST",

                        headers: {
                            "Content-Type": "application/json"
                        },

                        body: JSON.stringify({

                            page_title: pageData.title,
                            page_url: pageData.url,
                            page_text: pageData.text

                        })

                    }
                );

                const result = await backendResponse.json();

                isIndexed = true;

                response.textContent =
`✅ ${result.message}

Total Chunks: ${result.chunks}`;

            }

            catch (error) {

                console.error(error);

                response.textContent =
                    "❌ Failed to index page.";

            }

        }

    );

    // -------------------------------
    // Ask Question
    // -------------------------------

    askButton.addEventListener("click", async () => {

        const question = document
            .getElementById("question")
            .value
            .trim();

        if (!question) {

            response.textContent =
                "Please enter a question.";

            return;
        }

        if (!isIndexed) {

            response.textContent =
                "⏳ Please wait. Page is still being indexed.";

            return;
        }

        response.textContent =
            "🔍 Retrieving context...";

        try {

            const backendResponse = await fetch(
                "http://127.0.0.1:8000/retrieve",
                {

                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({

                        question: question

                    })

                }
            );

            const result = await backendResponse.json();

//             response.textContent =
// `✅ ${result.message}

// Retrieved Chunks: ${result.retrieved_chunks}`;
                response.textContent = result.answer;

        }

        catch (error) {

            console.error(error);

            response.textContent =
                "❌ Retrieval failed.";

        }

    });

});