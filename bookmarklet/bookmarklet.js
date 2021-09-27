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
  function save() {
    const ref = location.href
    const link = location.href
    fetch(`${ENDPOINT}/?referrer=${ref}&url=${link}&code=z`)
      .then((r) => r.json())
      .then((v) => {
        if (Notiflix) {
          Notiflix.Notify.success('saved successful')
        }
        console.log(v)
      }).catch((err) => {
        if (Notiflix) {
          Notiflix.Notify.failure('error occurred')
        }
        console.error(err)
      })
  }
  function main() {
    setup()
    save()
  }
  main()
})()
