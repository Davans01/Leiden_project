const baseUrl =
  process.env.NODE_ENV === "production"
    ? "https://api.ugleiden.test"
    : "http://localhost:5000"

export const request = async (url, data = undefined, headers = {}) => {
  const [method, path] = url.includes(" ") ? url.split(" ") : ["GET", url]

  const requestHeaders = new Headers()
  if (data) {
    requestHeaders.set("Content-Type", "application/json")
  }
  for (const [name, value] of Object.entries(headers)) {
    requestHeaders.set(name, value)
  }

  let response
  try {
    response = await fetch(baseUrl + path, {
      method,
      body: JSON.stringify(data),
      headers: requestHeaders,
      credentials: "include",
    })
  } catch (error) {
    console.error("Could not request API:", error)
    return {
      ok: false,
      status: 0,
      headers: new Headers(),
      data: undefined,
    }
  }

  let responseData = undefined
  const rawResponseData = await response.text()
  if (rawResponseData) {
    try {
      responseData = JSON.parse(rawResponseData)
    } catch (error) {
      responseData = rawResponseData
    }
  }

  return {
    ok: response.ok,
    status: response.status,
    headers: response.headers,
    data: responseData,
  }
}
