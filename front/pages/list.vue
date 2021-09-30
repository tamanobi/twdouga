<template>
  <div>
    <a-breadcrumb style="margin: 16px 0">
      <!-- <a-breadcrumb-item>Home</a-breadcrumb-item>
      <a-breadcrumb-item>List</a-breadcrumb-item>
      <a-breadcrumb-item>App</a-breadcrumb-item> -->
    </a-breadcrumb>
    <div class="container">
      <figure v-for="req in requests" :key="req.id">
        <video controls :src="req.video_url" :poster="req.thumbnail_url ? req.thumbnail_url : ''" />
        <figcaption><a :href="`https://twitter.com/i/status/${req.status}`"><a-icon type="twitter-circle" theme="filled" /></a><a :href="req.video_url"><a-icon type="zoom-in" /></a></figcaption>
      </figure>
      <infinite-loading
        spinner="spiral"
        :identifier="infiniteId"
        @infinite="infiniteHandler">
        <div slot="no-results">最後まで読み込みました</div>
      </infinite-loading>
    </div>
  </div>
</template>
<script>
function createFetchFunc(app) {
  return async (offset, limit) => {
    return await app.$service.listService.get(offset, limit);
  };
}
export default {
  async asyncData ({ app, params: {offset, limit} }) {
    offset = offset || 0;
    limit = limit || 10;

    const zfetch = createFetchFunc(app);
    return {
      zfetch,
      'list': (await zfetch(offset, limit)),
      load_completed: true,
      infiniteId: +new Date(),
    }
  },
  computed: {
    requests() {
      return this.list
    }
  },
  methods: {
    async infiniteHandler($state) {
      if (!this.load_completed) return;
      const res = await this.zfetch(this.list.length, 10);
      if (res.length === 0) {
        $state.complete();
        console.info("completed");
      } else {
        this.list = Array.prototype.concat(this.list, res);
        this.infiniteId += 1;
        console.log(this.list);
        $state.loaded();
        console.info("loaded");
      }
      this.infiniteId += 1;
    },
  }
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
.container {
  display: flex;
  flex-wrap: wrap;
  background: #fff;
  padding: 0;
  min-height: 280px;
}
.container > figure {
  position: relative;
  flex-grow:1;
  display: flex;
  flex-direction: column;
  margin: 2px;
}
.container > figure > video {
  height: 250px;
  object-fit: cover;
  max-width: 100%;
  min-width: 100%;
}
.container > figure > figcaption {
  position: absolute;
  right: 5px;
  top: 1px;
  z-index: 1;
  font-size: 24px;
}
</style>
