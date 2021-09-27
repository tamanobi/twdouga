;(function () {
  const ENDPOINT = 'https://cryptic-wildwood-50649.herokuapp.com'
  const LIBS = [
    'https://cdn.jsdelivr.net/npm/notiflix@3.0.2/dist/notiflix-aio-3.0.2.min.js',
  ]
  function loadScript(url) {
    const loaded = document.querySelector(`script[href='${url}']`)
    if (loaded) return
    script = document.createElement('script')
    script.src = url
    document.body.appendChild(script)
  }
  function setup() {
    LIBS.forEach((url) => loadScript(url))
  }
  function onClick(evt) {
    const ref = location.href
    const link = evt.target.parentElement.href
    if (Notiflix) Notiflix.Notify.info('saving')
    evt.target.disabled = true
    evt.target.textContent = 'saving'
    fetch(`${ENDPOINT}/?referrer=${ref}&url=${link}&code=z`)
      .then((r) => r.json())
      .then((v) => {
        if (Notiflix) {
          Notiflix.Notify.success('saved successful')
        }
        evt.target.disabled = true
        evt.target.textContent = 'Saved'
        console.log(v)
      })
      .catch((err) => {
        if (Notiflix) {
          Notiflix.Notify.failure('error occurred')
        }
        evt.target.disabled = false
        evt.target.textContent = 'Save URL'
        console.error(err)
      })
    return false
  }
  function buildButton() {
    var a = document.createElement('button')
    a.textContent = 'Save URL'
    a.onclick = onClick
    return a
  }
  function setButton() {
    Array.from(
      document.querySelectorAll('.content a:not([data-has-save-button]) > img')
    ).forEach((v) => {
      v.parentElement.dataset.hasSaveButton = true
      v.parentElement.appendChild(buildButton())
    })
  }
  ;(function main() {
    setup()
    setInterval(() => {
      setButton()
    }, 1000)
  })()
})()
