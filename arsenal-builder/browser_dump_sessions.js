// Dump every Arsenal session (title, abstract, speakers, tracks) from a Black Hat
// schedule page.
//
// The schedule pages (https://www.blackhat.com/<event>/arsenal/schedule/index.html,
// archived at https://blackhat.com/archive/<region>/<year>/arsenal/schedule/) load a
// sessions.json into `window.data.sessions`. Cloudflare blocks plain HTTP clients,
// so run this in the browser: open the page, paste this file into the DevTools
// console (or run it through a browser-automation tool), then copy the result.
//
// Returns an array of {id, title, description, speakers, tracks, format, type}.
// `description` is the abstract with HTML tags removed.
(() => {
  const strip = (html) => {
    const el = document.createElement("div");
    el.innerHTML = (html || "").replace(/<br\s*\/?>/gi, "\n");
    return el.textContent.replace(/\s*\n\s*/g, " ").replace(/\s{2,}/g, " ").trim();
  };
  const speakersById = {};
  for (const s of Object.values(window.data?.speakers || {})) {
    const id = s.id ?? s.person_id;
    speakersById[id] = [s.first_name, s.last_name].filter(Boolean).join(" ").trim() || s.name || "";
  }
  const sessions = Object.values(window.data?.sessions || {});
  return sessions
    .filter((s) => /arsenal/i.test(`${s.type || ""} ${s.program || ""} ${s.discipline_1 || ""}`))
    .map((s) => ({
      id: s.id,
      title: (s.title || "").trim(),
      description: strip(s.description),
      speakers: (s.speakers || [])
        .map((sp) => speakersById[sp.person_id ?? sp.id] || sp.name || "")
        .filter(Boolean),
      tracks: [s.track_1, s.track_2].filter(Boolean),
      format: s.format || "",
      type: s.type || "",
    }));
})();
