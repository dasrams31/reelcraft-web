document.addEventListener("DOMContentLoaded", () => {
    const generateForm = document.getElementById("generateForm");
    const destInput = document.getElementById("destInput");
    const toneSelect = document.getElementById("toneSelect");
    const emptyState = document.getElementById("emptyState");
    const loadingState = document.getElementById("loadingState");
    const resultState = document.getElementById("resultState");
    const btnGenerate = document.getElementById("btnGenerate");
    
    const audioPlayer = document.getElementById("audioPlayer");
    const audioTitle = document.getElementById("audioTitle");
    const btnDownloadMp3 = document.getElementById("btnDownloadMp3");
    const btnDownloadSrt = document.getElementById("btnDownloadSrt");
    
    const scenesContainer = document.getElementById("scenesContainer");
    const fullScriptBox = document.getElementById("fullScriptBox");
    const captionBox = document.getElementById("captionBox");
    const destBadge = document.getElementById("destBadge");
    
    const btnCopyScript = document.getElementById("btnCopyScript");
    const btnCopyCaption = document.getElementById("btnCopyCaption");

    // Quick tag clicks
    document.querySelectorAll("#quickTags span").forEach(tag => {
        tag.addEventListener("click", () => {
            destInput.value = tag.getAttribute("data-dest");
            destInput.focus();
        });
    });

    // Duration radio styling
    document.querySelectorAll("input[name='duration']").forEach(radio => {
        radio.addEventListener("change", (e) => {
            document.querySelectorAll(".duration-card").forEach(card => {
                card.classList.remove("active", "border-brand-500", "bg-brand-500/10", "text-white");
                card.classList.add("border-dark-600", "bg-dark-900", "text-gray-400");
            });
            const parent = radio.closest(".duration-card");
            parent.classList.add("active", "border-brand-500", "bg-brand-500/10", "text-white");
            parent.classList.remove("border-dark-600", "bg-dark-900", "text-gray-400");
        });
    });

    // Voice radio styling
    document.querySelectorAll("input[name='voice']").forEach(radio => {
        radio.addEventListener("change", (e) => {
            document.querySelectorAll(".voice-card").forEach(card => {
                card.classList.remove("active", "border-brand-500", "bg-brand-500/10", "text-white");
                card.classList.add("border-dark-600", "bg-dark-900", "text-gray-400");
            });
            const parent = radio.closest(".voice-card");
            parent.classList.add("active", "border-brand-500", "bg-brand-500/10", "text-white");
            parent.classList.remove("border-dark-600", "bg-dark-900", "text-gray-400");
        });
    });

    // Tabs switching
    const tabBtns = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");

    tabBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            tabBtns.forEach(b => {
                b.classList.remove("active", "border-brand-500", "text-brand-400");
                b.classList.add("border-transparent", "text-gray-400");
            });
            tabContents.forEach(c => c.classList.add("hidden"));

            btn.classList.add("active", "border-brand-500", "text-brand-400");
            btn.classList.remove("border-transparent", "text-gray-400");

            const target = btn.getAttribute("data-tab");
            document.getElementById(target).classList.remove("hidden");
        });
    });

    // Copy handlers
    btnCopyScript.addEventListener("click", () => {
        navigator.clipboard.writeText(fullScriptBox.innerText);
        btnCopyScript.innerHTML = `<i class="fa-solid fa-check text-green-400"></i> Tersalin!`;
        setTimeout(() => {
            btnCopyScript.innerHTML = `<i class="fa-solid fa-copy"></i> Salin Naskah`;
        }, 2000);
    });

    btnCopyCaption.addEventListener("click", () => {
        navigator.clipboard.writeText(captionBox.innerText);
        btnCopyCaption.innerHTML = `<i class="fa-solid fa-check text-green-400"></i> Tersalin!`;
        setTimeout(() => {
            btnCopyCaption.innerHTML = `<i class="fa-solid fa-copy"></i> Salin Caption`;
        }, 2000);
    });

    // Generate Submit
    generateForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const destination = destInput.value.trim();
        if (!destination) return;

        const duration = parseInt(document.querySelector("input[name='duration']:checked").value);
        const voice = document.querySelector("input[name='voice']:checked").value;
        const tone = toneSelect.value;

        // UI Loading State
        emptyState.classList.add("hidden");
        resultState.classList.add("hidden");
        loadingState.classList.remove("hidden");
        btnGenerate.disabled = true;
        btnGenerate.classList.add("opacity-50", "cursor-not-allowed");

        try {
            const response = await fetch("/api/generate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ destination, duration, tone, voice })
            });

            if (!response.ok) {
                const err = await response.json();
                throw new Error(err.detail || "Gagal menghasilkan konten");
            }

            const data = await response.json();
            const sb = data.storyboard;

            // Update Audio Player
            audioPlayer.src = data.audio_url;
            audioTitle.textContent = `Narasi ${sb.destination} (${sb.duration}s)`;
            btnDownloadMp3.href = data.audio_url;
            btnDownloadMp3.download = data.audio_filename;
            btnDownloadSrt.href = data.srt_url;
            btnDownloadSrt.download = data.srt_filename;

            destBadge.textContent = `${sb.destination} • ${sb.elevation}`;

            // Render Storyboard Scenes
            scenesContainer.innerHTML = "";
            sb.scenes.forEach((sc, idx) => {
                const sceneDiv = document.createElement("div");
                sceneDiv.className = "scene-card bg-dark-900 border border-dark-600 rounded-xl p-4 space-y-2.5";
                sceneDiv.innerHTML = `
                    <div class="flex items-center justify-between border-b border-dark-700 pb-2">
                        <span class="text-xs font-bold text-brand-400 flex items-center gap-1.5">
                            <i class="fa-solid fa-clock text-[10px]"></i> ${sc.time}
                        </span>
                        <span class="text-[10px] text-gray-400 font-mono px-2 py-0.5 rounded bg-dark-800 border border-dark-700">Scene #${idx + 1}</span>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                        <div class="space-y-1">
                            <div class="text-[11px] font-semibold text-gray-400 flex items-center gap-1">
                                <i class="fa-solid fa-video text-purple-400"></i> Arahan Visual (B-Roll):
                            </div>
                            <p class="text-gray-200 leading-relaxed">${sc.visual}</p>
                        </div>
                        <div class="space-y-1">
                            <div class="text-[11px] font-semibold text-gray-400 flex items-center gap-1">
                                <i class="fa-solid fa-microphone text-blue-400"></i> Naskah Voiceover (VO):
                            </div>
                            <p class="text-gray-200 italic leading-relaxed">"${sc.voiceover}"</p>
                        </div>
                    </div>
                    <div class="text-[10px] text-gray-500 pt-1 flex items-center gap-1">
                        <i class="fa-solid fa-music text-amber-500"></i> <span class="font-medium text-gray-400">SFX/Audio:</span> ${sc.sfx}
                    </div>
                `;
                scenesContainer.appendChild(sceneDiv);
            });

            // Render Full Script & Caption
            fullScriptBox.textContent = sb.full_voiceover;
            captionBox.textContent = sb.caption;

            // Switch to result view
            loadingState.classList.add("hidden");
            resultState.classList.remove("hidden");

        } catch (err) {
            alert("Terjadi kesalahan: " + err.message);
            loadingState.classList.add("hidden");
            emptyState.classList.remove("hidden");
        } finally {
            btnGenerate.disabled = false;
            btnGenerate.classList.remove("opacity-50", "cursor-not-allowed");
        }
    });
});
