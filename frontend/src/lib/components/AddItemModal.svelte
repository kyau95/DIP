<script lang="ts">
  import { postProductUrl } from "$lib/api";
  import Banner from "$lib/components/Banner.svelte";

  let { showModal = $bindable() } = $props();

  let url = $state("");
  let errorMessage = $state("");
  let successMessage = $state("");
  let isLoading = $state(false);

  const handleKeydown = (event: KeyboardEvent) => {
    if (showModal && event.key === "Escape") {
      showModal = false;
    }
  };
</script>

<svelte:window onkeydown={handleKeydown} />

{#if showModal}
  <div class="overlay">
    <div class="modal-panel">
      <div class="modal-header">Add a New Item</div>
      <Banner {...{ errorMessage, successMessage, isLoading }} />
      <div class="modal-body">
        <label for="url">Product URL</label>
        <input
          autocomplete="off"
          type="text"
          id="url"
          placeholder="https://example.com"
          bind:value={url}
        />
      </div>
      <div class="modal-footer">
        <button class="cancel" onclick={() => (showModal = false)}
          >Cancel</button
        >
        <button
          class="active"
          onclick={async () => {
            errorMessage = "";
            successMessage = "";
            isLoading = true;

            try {
              const product = await postProductUrl(url);
              console.log(product);
              successMessage = `Added ${product.productName}`;
              url = "";
            } catch (err) {
              errorMessage =
                err instanceof Error
                  ? err.message
                  : "An unknown error occurred";
            } finally {
              isLoading = false;
            }
          }}>Add Item</button
        >
      </div>
    </div>
  </div>
{/if}

<style>
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(15, 23, 42, 0.3);
    backdrop-filter: blur(8px);
    z-index: 999;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal-panel {
    background-color: white;
    border-radius: 16px;
    box-shadow:
      0 20px 25px -5px rgba(0, 0, 0, 0.1),
      0 10px 10px -5px rgba(0, 0, 0, 0.04);
    width: 90%;
    max-width: 480px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    border: 1px solid #f1f5f9;
  }

  .modal-header {
    padding: 24px 24px 16px 24px;
    font-size: 1.5rem;
    font-weight: 700;
    color: #0f172a;
    border-bottom: 1px solid #f1f5f9;
  }

  .modal-body {
    padding: 36px 24px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  label {
    font-size: 1rem;
    font-weight: 600;
    color: #475569;
  }

  input {
    border-radius: var(--default-border-radius);
    font-size: 1rem;
    padding: 10px 14px;
    border: 1px solid #cbd5e1;
    width: 100%;
    box-sizing: border-box;
    outline: none;
    transition:
      border-color 0.15s ease,
      box-shadow 0.15s ease;
  }

  input:focus {
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
  }

  .modal-footer {
    padding: 16px 24px 24px 24px;
    background-color: #f8fafc;
    display: flex;
    justify-content: flex-end;
    gap: 12px;
    border-top: 1px solid #f1f5f9;
  }

  button {
    border-radius: var(--default-border-radius);
    padding: 12px 32px;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
    border: none;
    transition:
      background-color 0.2s ease,
      transform 0.1s ease,
      box-shadow 0.2s ease;
  }

  button:active {
    transform: scale(0.96);
  }

  .cancel {
    background-color: #f3f4f6;
    color: #4b5563;
  }

  .cancel:hover {
    background-color: #e5e7eb;
  }

  .active {
    background-color: #3b82f6;
    color: white;
    box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.2);
  }

  .active:hover {
    background-color: #2563eb;
    box-shadow: 0 6px 10px -1px rgba(59, 130, 246, 0.3);
  }
</style>
