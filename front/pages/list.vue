<template>
  <div>
    <a-breadcrumb style="margin: 16px 0">
      <!-- <a-breadcrumb-item>Home</a-breadcrumb-item>
      <a-breadcrumb-item>List</a-breadcrumb-item>
      <a-breadcrumb-item>App</a-breadcrumb-item> -->
    </a-breadcrumb>
    <div class="container">
      <div class="box" v-for="req in requests" :key="req.id">
        <figure>
          <video controls :src="req.video_url" :poster="req.thumbnail_url ? req.thumbnail_url : ''" />
          <figcaption><a :href="`https://twitter.com/i/status/${req.status}`"><a-icon type="twitter-circle" theme="filled" /></a><a :href="req.video_url"><a-icon type="zoom-in" /></a></figcaption>
        </figure>
      </div>

      <div v-if="!load_completed" ref="scroll_trigger" style="display: flex;justify-content: center;width: 100%;margin: 32px 0;">
        <a-icon type="loading" style="font-size: 64px;" />
      </div>
      <div v-else>最後まで読み込みました</div>
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
  head() {
    return {
      title: "Twitter の注目動画",
    }
  },
  mounted: function mounted() {
    this.observer = new IntersectionObserver((entries) => {
      const entry = entries[0];
      if (entry && entry.isIntersecting) {
        let promise = this.infiniteHandler(this.$state);
        for (let i = 1; i <= 30; ++i) {
          promise = promise.catch((error) => {
            if (error) {
              setTimeout(async () => {
                await this.infiniteHandler(this.$state)
              }, 5000)
            }
          });
        }
        promise.then().catch();
      }
    });

    this.observer.observe(this.$refs.scroll_trigger);
  },
  async asyncData ({ app, params: {offset, limit} }) {
    offset = offset || 0;
    limit = limit || 30;

    const zfetch = createFetchFunc(app);
    return {
      observer: null,
      zfetch,
      'list': (await zfetch(offset, limit)),
      load_completed: false,
    }
  },
  computed: {
    requests() {
      return this.list
    }
  },
  methods: {
    async infiniteHandler($state) {
      if (this.load_completed) return;
      const res = await this.zfetch(this.list.length, 30);
      if (res.length === 0) {
        $state.complete();
      } else {
        this.list = Array.prototype.concat(this.list, res);
        $state.loaded();
      }
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
.container > .box {
  padding: 0;
  position: relative;
  flex-grow:1;
  display: flex;
  flex-direction: column;
  margin: 2px;
}
.container > .box > figure {
  margin: 0;
  padding: 0;
}
.container > .box > figure > video {
  margin: 0;
  padding: 0;
  height: 250px;
  object-fit: cover;
  max-width: 100%;
  min-width: 100%;
}
.container > .box > figure > figcaption {
  position: absolute;
  right: 5px;
  top: 1px;
  z-index: 1;
  font-size: 24px;
}
</style>
