<template>
  <view class="content">
    <Header :isHome="false" title="首页"></Header>
    <view class="mt5">
      
    </view>
    Hello
    <image class="logo pngshadow" src="/static/logo.png" @click="handleLogo"></image>
    <view class="text-area">
      <text class="title">{{ title }}</text>
    </view>
  </view>
</template>

<script>
import Header from '../../components/header/Header.vue';
export default {
  components: {
    Header,
  },
  data() {
    return {
      title: 'Hello'
    };
  },
  onLoad() {},
  methods: {
    handleLogo() {
      uni.navigateTo({
        url: '/pages/test/test'
      })
    }
  }
};
</script>

<style scoped>
@import '../../static/css/global.scss';
.content {
  display: flex;
  flex-direction: column;
  height: 200vh;
}

.logo {
  height: 200rpx;
  width: 200rpx;
  margin-top: 200rpx;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 50rpx;
}

.text-area {
  display: flex;
  justify-content: center;
}

.title {
  font-size: 36rpx;
  color: #8f8f94;
}
</style>
