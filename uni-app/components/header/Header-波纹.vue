<template>
  <view class="content smallshadow midradius borderbox">
    <view class="square-back"></view>
    <view class="cicle-back circleradius"></view>
    <view class="square-mid"></view>
    <view class="cicle-front circleradius"></view>
  </view>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: '导航栏'
    },
    color: {
      type: String,
      default: 'blue'
    },
    isHome: {
      type: Boolean,
      default: false
    },
    height: {
      type: Number,
      default: 100
    }
  },
  data() {
    return {};
  },
  methods: {},
  mounted() {}
};
</script>

<style scoped>
@import '../../static/css/global.scss';

.content {
  height: 100rpx;
  width: 90%;
  left: 5%;
  top: 20rpx;
  overflow: hidden;
  position: fixed;
  /* background-color: #005EFF; */
  border: none;
}

.square-back {
  position: absolute;
  background-color: #005eff;
  width: 500rpx;
  height: 500rpx;
  top: -200rpx;
  right: -100rpx;
  z-index: 1500;
}

.cicle-back {
  position: absolute;
  background-color: #478bff;
  width: 500rpx;
  height: 500rpx;
  top: -200rpx;
  left: -150rpx;
  z-index: 2000;
}

.square-mid {
  position: absolute;
  width: 500rpx;
  height: 500rpx;
  background-color: #eeeeee;
  top: -200rpx;
  left: -260rpx;
  z-index: 2500;
}

.cicle-front {
  position: absolute;
  background-color: #eeeeee;
  width: 500rpx;
  height: 500rpx;
  top: -200rpx;
  left: -250rpx;
  z-index: 3000;
}
</style>
