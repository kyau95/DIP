<script lang="ts">
  import { postProductUrl } from "$lib/api";

  let { showModal = $bindable() } = $props();
  let url = $state("");
</script>

{#if showModal}
  <div class="overlay">
    <div class="modal-panel">
      <div class="modal-header">
        Add a New Item
        <hr />
      </div>
      <div class="modal-body">
        <label for="url">Product URL</label>
        <br />
        <input
          autocomplete="off"
          type="text"
          id="url"
          placeholder="https://example.com"
          bind:value={url}
        />
        <hr />
      </div>
      <div class="modal-footer">
        <button class="cancel" onclick={() => (showModal = false)}
          >Cancel</button
        >
        <button
          class="active"
          onclick={() => {
            console.log(url);
            // postProductUrl(url);
            url = "";
          }}>Add</button
        >
      </div>
    </div>
  </div>
{/if}

<style>
  hr {
    margin-top: 6px;
    margin-bottom: 0;
  }

  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.7);
    z-index: 999;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal-panel {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
    width: 90%;
    max-width: 500px;
  }

  .modal-header {
    padding: 24px 16px 0 16px;
    font-size: 1.5em;
    font-weight: bold;
  }

  .modal-body {
    padding: 8px 16px;
  }

  .modal-footer {
    padding: 0 16px 20px 16px;
    display: flex;
    justify-content: flex-end;
    gap: 10px;
  }

  input {
    border-radius: var(--default-border-radius);
    font-size: 1rem;
    margin: 8px 0;
    padding: 12px 8px;
    width: 95%;
  }

  button {
    border-radius: var(--default-border-radius);
    padding: 10px 24px;
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
