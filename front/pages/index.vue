<template>
  <div>
    <a-breadcrumb style="margin: 16px 0">
      <!-- <a-breadcrumb-item>Home</a-breadcrumb-item>
      <a-breadcrumb-item>List</a-breadcrumb-item>
      <a-breadcrumb-item>App</a-breadcrumb-item> -->
    </a-breadcrumb>
    <div :style="{ background: '#fff', padding: '24px', minHeight: '280px' }">
      <a-row type="flex" justify="center" align="top">
        <a-col :xs="24" :sm="24" :md="24" :lg="12">
          <p>ツイートのURLを入力すると動画が保存できます</p>
          <a-input v-model="inputUrl" allow-clear placeholder="twitter の url 例: https://twitter.com/hybridcIena/status/1441113107598770178" :disabled="loading" size="large">
            <a-icon slot="prefix" type="twitter" />
          </a-input>
          <br />
          <br />
          <a-button type="primary" size="large" :loading="loading" @click="getVideo">動画のURLを手に入れる</a-button>
          <br />
          <br />
          <a-spin :spinning="loading">
            <div class="spin-content">
              <div v-if="videoUrl">
                <video controls style="max-width: 100%;">
                  <source :src="videoUrl" type="video/mp4"/>
                </video>
                <p><a :href="videoUrl">{{ videoUrl }}</a></p>
              </div>
              <div v-else>ここに動画が表示されます</div>
            </div>
          </a-spin>
        </a-col>
      </a-row>
    </div>
  </div>
</template>
<script>
export default {
  head() {
    return {
      title: "Twitter 動画を取得"
    }
  },
  data() {
    return {
      inputUrl: '',
      loading: false,
      videoUrl: ''
    };
  },
  methods: {
    async getVideo() {
      if (this.inputUrl === '' || !this.inputUrl.startsWith("https://") || !this.inputUrl.includes("twitter.com/") || !this.inputUrl.includes("status/")) {
        this.$message.error('Twitter の URL を入力してください');
        return;
      }
      this.loading = true;
      const endpoint = process.env.ENDPOINT;
      const url = `${endpoint}?url=${encodeURIComponent(this.inputUrl)}`;
			const response = await this.$axios.$get(url);
      if (!response) {
        this.$message.error('予期しないエラーが発生しました。しばらく経ってからお試しください');
        return;
      }
      this.loading = false;
      this.videoUrl = response.url;
      this.inputUrl = "";
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
.spin-content {
  border: 1px solid #91d5ff;
  background-color: #e6f7ff;
  padding: 30px;
}
</style>
