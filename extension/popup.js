
document.addEventListener("DOMContentLoaded", async () => {



    const askButton = document.getElementById("askButton");
    const response = document.getElementById("response");
    const copyButton = document.getElementById("copyButton");
    copyButton.style.display = "none";

    const pageTitle =document.getElementById("pageTitle");

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
                pageTitle.textContent ="Unsupported page";

                console.error(chrome.runtime.lastError.message);

                return;
            }

            if (!data) {

                response.textContent =
                    "❌ No page data received.";
                pageTitle.textContent ="Unknown page";

                return;
            }

            pageData = data;
            // pageTitle.textContent =pageData.title;
            pageTitle.textContent =
                pageData.title.length > 60
                    ? pageData.title.substring(0, 60) + "..."
                    : pageData.title;

            response.textContent = "📄 Indexing page...";
            copyButton.style.display = "none";

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
        copyButton.style.display = "none";

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

            response.textContent = result.answer;

            copyButton.style.display = "block";


        }

        catch (error) {

            console.error(error);

            response.textContent =
                "❌ Retrieval failed.";
            copyButton.style.display = "none";

        }

    });

    copyButton.addEventListener("click", async () => {

        const answer = response.textContent;

        if (!answer.trim()) return;

        await navigator.clipboard.writeText(answer);

        copyButton.textContent = "✅ Copied!";

        setTimeout(() => {

            copyButton.textContent = "📋 Copy Answer";

        }, 1500);

    });

});