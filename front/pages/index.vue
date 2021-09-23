<template>
  <a-layout id="components-layout-demo-top" class="layout">
    <a-layout-header>
      <div class="logo">twdouga</div>
      <a-menu
        theme="dark"
        mode="horizontal"
        :default-selected-keys="['1']"
        :style="{ lineHeight: '64px' }"
      >
        <a-menu-item key="1">
          動画保存
        </a-menu-item>
      </a-menu>
    </a-layout-header>
    <a-layout-content style="padding: 0 50px">
      <a-breadcrumb style="margin: 16px 0">
        <!-- <a-breadcrumb-item>Home</a-breadcrumb-item>
        <a-breadcrumb-item>List</a-breadcrumb-item>
        <a-breadcrumb-item>App</a-breadcrumb-item> -->
      </a-breadcrumb>
      <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
        <a-input v-model="inputUrl" placeholder="twitter の url 例: https://twitter.com/hybridcIena/status/1441113107598770178" :disabled="loading" size="large">
          <a-icon slot="prefix" type="twitter" />
          <a-tooltip slot="suffix" title="Extra information">
            <a-icon type="info-circle" style="color: rgba(0,0,0,.45)" />
          </a-tooltip>
        </a-input>
        <br />
        <br />
        <a-button type="primary" size="large" :disabled="loading" @click="test">動画のURLを手に入れる</a-button>
        <br />
        <br />
        <div v-if="videoUrl">
          <video controls>
            <source :src="videoUrl" type="video/mp4"/>
          </video>
          <p>
            <a :href="videoUrl">{{ videoUrl }}</a>
          </p>
          <p>
            <a :href="videoUrl" download>ダウンロード</a>
          </p>
        </div>
      </div>
    </a-layout-content>
    <a-layout-footer style="text-align: center">
      twdouga ©2021
    </a-layout-footer>
  </a-layout>
</template>

<script>
export default {
  data() {
    return {
      inputUrl: '',
      loading: false,
      videoUrl: ''
    };
  },
  methods: {
    async test() {
      this.loading = true;
      const endpoint = "https://safe-sands-65135.herokuapp.com/";
      const url = `${endpoint}?url=${encodeURIComponent(this.inputUrl)}`;
			const response = await this.$axios.$get(url);
      this.loading = false;
      this.videoUrl = response.url;
    },
  },
};
</script>
<style>
#components-layout-demo-top .logo {
  width: 120px;
  height: 31px;
  background: rgba(255, 255, 255, 0.2);
  margin: 16px 24px 16px 0;
  float: left;
  vertical-align: top;
  color: white;
}
</style>
