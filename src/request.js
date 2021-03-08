export const request = async (url, data = undefined, headers = {}) => {
  const [method, path] = url.includes(" ") ? url.split(" ") : ["GET", url]

  const requestHeaders = new Headers()
  if (data) {
    requestHeaders.set("Content-Type", "application/json")
  }
  for (const [name, value] of Object.entries(headers)) {
    requestHeaders.set(name, value)
  }

  const response = await fetch(`http://localhost:5000${path}`, {
    method,
    body: JSON.stringify(data),
    headers: requestHeaders,
    credentials: "include",
  })

  let responseData = undefined
  if (response.ok) {
    const json = await response.text()
    if (json) {
      responseData = JSON.parse(json)
    }
  }

  return {
    ok: response.ok,
    status: response.status,
    headers: response.headers,
    data: responseData,
  }
}
