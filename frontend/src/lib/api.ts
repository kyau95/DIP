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

export const getPriceHistory = async () => {
    const resp = await fetch(
        `${API_URL}/api/price_history`
    );

    if (!resp.ok) {
        throw new Error("Failed to fetch price related history");
    }
    return await resp.json();
}

export const postProductUrl = async (url: string) => {
    const resp = await fetch(
        `${API_URL}/api/products`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ url }),
        }
    )

    if (!resp.ok) {
        throw new Error("Failed to add product");
    }

    return await resp.json();
}