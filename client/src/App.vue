<script setup lang="ts">
import TakePictureBtn from './components/take-picture-btn.vue';
import UploadBtn from './components/upload-btn.vue';
import StartReading from './components/start-reading.vue';
</script>

<template>
  <main>
    <h1 class="title">Interactive reading assistant</h1>
    <textarea name="text-to-analyze" id=""></textarea>
    <div class="buttons-group">
      <UploadBtn />
      <TakePictureBtn />
      <StartReading />
    </div>
  </main>
</template>

<style>
main {
  padding: 40px;
  margin: auto;
  background: #f9fafb;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.title {
  font: var(--font-title)
}

textarea {
  border: var(--base-border);
  border-radius: var(--base-radius);
  width: 100%;
  height: 150px;
  background: var(--base-white);
}

.buttons-group {
  display: flex;
  align-items: center;
  gap: 12px;
}
</style>
