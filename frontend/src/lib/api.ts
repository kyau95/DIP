// place files you want to import through the `$lib` alias in this folder.

const API_URL = "http://localhost:8000";

export const getProducts = async () => {
    const resp = await fetch(
        `${API_URL}/api/products`  
    );

    if (!resp.ok) {
        throw new Error("Failed to fetch products");
    }
    return await resp.json();
}