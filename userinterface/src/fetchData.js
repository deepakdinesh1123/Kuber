export async function fetchDataFromApi(sandboxId, containerId, path) {
  const apiUrl = `http://localhost:8000/sandbox/${sandboxId}/container/${containerId}/folder`;
  console.log(apiUrl);

  const requestData = {
    path: path,
  };

  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(requestData),
  };

  try {
    const response = await fetch(apiUrl, requestOptions);

    if (!response.ok) {
      throw new Error("API request failed");
    }

    const responseData = await response.json();
    return responseData;
  } catch (error) {
    console.error("Error fetching data from API:", error);
    return null;
  }
}
