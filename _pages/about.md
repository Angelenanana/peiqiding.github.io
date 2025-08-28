---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I'm **Peiqi Ding** (Chinese: 丁沛琦), presently a fourth-year undergraduate student studying Clinical Medicine at [The Second Norman Bethune Hospital](http://113.45.131.203:9099/home), [Jilin University (JLU)](https://www.jlu.edu.cn/).

I have been actively collaborating with [Doc. Wu](http://113.45.131.203:9099/zjtd/yjks23/ykyy32/ydbk2/content_101151) and [Doc. Qu](https://medicine.jlu.edu.cn/info/1251/13274.htm). My research interests lie primarily in **Posterior Segment Diseases**, particularly **macular disease** and related conditions.

I am open to any research collaboration. Feel free to contact me via [Email](dingpq9922@163.com) or <a href="#" onclick="showWeChatQR(); return false;">WeChat</a>.

<!-- WeChat QR Code Modal -->
<div id="wechatModal" style="display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.5);" onclick="closeWeChatQR()">
  <div style="position: relative; margin: 10% auto; width: 300px; background: white; border-radius: 16px; padding: 2em; text-align: center; box-shadow: 0 8px 32px rgba(0,0,0,0.3);" onclick="event.stopPropagation()">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1em;">
      <h3 style="margin: 0; color: #2d3748; font-size: 1.2em;">WeChat QR Code</h3>
      <span style="cursor: pointer; font-size: 1.5em; color: #999; font-weight: bold;" onclick="closeWeChatQR()">&times;</span>
    </div>
    <img src="images/wechat-qr.png" alt="WeChat QR Code" style="width: 200px; height: 200px; border-radius: 12px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1); margin: 1em 0;" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';" />
    <div style="display: none; padding: 1em; background: #f8f9fa; border-radius: 8px; color: #666; font-size: 0.9em;">
      📱 WeChat QR code will be displayed here<br>
      <small>Please add wechat-qr.png to the images/ folder</small>
    </div>
    <p style="color: #666; font-size: 0.9em; margin: 1em 0 0 0;">Scan to add me on WeChat</p>
  </div>
</div>

<script>
function showWeChatQR() {
  document.getElementById('wechatModal').style.display = 'block';
  document.body.style.overflow = 'hidden'; // 防止背景滚动
}

function closeWeChatQR() {
  document.getElementById('wechatModal').style.display = 'none';
  document.body.style.overflow = 'auto'; // 恢复滚动
}

// ESC键关闭弹窗
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeWeChatQR();
  }
});
</script>

# 🔥 News

- **2025.8** 🏆 Won **Second Prize** in China Undergraduate Medical Innovation Tournament & The Belt and Road International Competition
- **2025.7** 🏆 Won **Third Prize** in China Undergraduate Life Science Contest (Scientific Inquiry Category)
- **2024.11** 🎖️ Awarded **Lei Jun Computer Undergraduate Scholarship** (¥10000)

<!--
# 📝 Publications 
*前面的世界，以后再来探索吧*
-->

# 📃 Publications

<div class="section-description" style="color: #666; font-size: 0.9em; margin-bottom: 2em; display: flex; justify-content: space-between; align-items: center;">
  <span>† Equal Contribution</span>
  <div class="year-badge" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.3em 1em; border-radius: 20px; font-size: 0.9em; font-weight: 600;">2025</div>
</div>

<div class="paper-box" style="display: flex; gap: 2em; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1.5em; margin-bottom: 1.5em; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);">
  <div class="paper-content" style="flex: 1;">
    <h3 style="color: #1a202c; font-size: 1.2em; font-weight: 600; margin: 0 0 0.8em 0;">Risk factors for pterygium: latest research progress on major pathogenesis</h3>
    
    <div style="color: #4a5568; font-size: 0.95em; margin-bottom: 0.8em;">
      <strong style="color: #2d3748;">Peiqi Ding</strong>, Ruiqing Wang, Yuqian He, <em>et al.</em>
    </div>
    
    <div style="color: #6b7280; font-size: 0.9em; font-style: italic;">
      Experimental Eye Research（Q2，IF=3.77）
    </div>
  </div>
  
  <div style="flex: 0 0 160px;">
    <img src="images/paper1.jpg" alt="Pterygium Research Framework" style="width: 100%; border-radius: 8px; border: 1px solid #e2e8f0;" />
  </div>
</div>

<div class="paper-box" style="display: flex; gap: 2em; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1.5em; margin-bottom: 1.5em; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);">
  <div class="paper-content" style="flex: 1;">
    <h3 style="color: #1a202c; font-size: 1.2em; font-weight: 600; margin: 0 0 0.8em 0;">Targeting mechanotransduction in osteosarcoma</h3>
    
    <div style="color: #4a5568; font-size: 0.95em; margin-bottom: 0.8em;">
      <strong style="color: #2d3748;">Ruoyun He</strong>, <strong style="color: #2d3748;">Peiqi Ding</strong>†, <strong style="color: #2d3748;">Yanan She</strong>† <em>et al.</em>
    </div>
    
    <div style="color: #6b7280; font-size: 0.9em; font-style: italic;">
      Biochem Biophys Res Commun（Q3，IF=2.2）
    </div>
  </div>
  
  <div style="flex: 0 0 160px;">
    <img src="images/paper2.jpg" alt="Osteosarcoma Research" style="width: 100%; border-radius: 8px; border: 1px solid #e2e8f0;" />
  </div>
</div>

# 🏆 Competition Awards

<div class="award-item">
  <span class="award-medal">🥈 Second Prize</span>
  <div class="award-details">
    <div class="award-title">China Undergraduate Medical Innovation Tournament & The Belt and Road International Competition</div>
    <div class="award-year">2025</div>
  </div>
</div>

<div class="award-item">
  <span class="award-medal bronze">🥉 Third Prize</span>
  <div class="award-details">
    <div class="award-title">China Undergraduate Life Science Contest (Scientific Inquiry Category)</div>
    <div class="award-year">2025</div>
  </div>
</div>

<div class="award-item">
  <span class="award-medal silver">🥈 Second Prize</span>
  <div class="award-details">
    <div class="award-title">China International College Students Innovation Competition</div>
    <div class="award-location">(Jilin University Region)</div>
    <div class="award-year">2024</div>
  </div>
</div>

<div class="award-item">
  <span class="award-medal silver">🥈 Silver Medal</span>
  <div class="award-details">
    <div class="award-title">International Genetically Engineered Machine competition</div>
    <div class="award-location">(Paris, France)</div>
    <div class="award-year">2023</div>
  </div>
</div>


# 🎖 Scholarships and Honors

<div class="scholarship-item">
  <div class="scholarship-title">Dong Rong Scholarship</div>
  <div class="scholarship-details">
    <strong>Award Rate:</strong> 10/1213 • <em>Jilin University & IB Group Korea</em> • <strong>2024</strong>
  </div>
</div>

<div class="scholarship-item">
  <div class="scholarship-title">First Class Scholarship of JLU</div>
  <div class="scholarship-details">
    <strong>Award Rate:</strong> 5% school-wide • <em>Jilin University</em> • <strong>2024</strong>
  </div>
</div>

<div class="scholarship-item">
  <div class="scholarship-title">Outstanding Communist Youth League Member of Jilin University</div>
  <div class="scholarship-details">
    <strong>Award Rate:</strong> 5% school-wide • <em>Jilin University</em> • <strong>2024</strong>
  </div>
</div>

<div class="scholarship-item">
  <div class="scholarship-title">Merit Student</div>
  <div class="scholarship-details">
    <strong>Award Rate:</strong> 10% school-wide • <em>Jilin University</em> • <strong>2023, 2024</strong>
  </div>
</div>




# 📖 Education

<div style="background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%); border: 1px solid #e1e8f7; border-radius: 16px; padding: 2em; margin-bottom: 2em; box-shadow: 0 4px 20px rgba(102, 126, 234, 0.1); transition: all 0.3s ease;">
  <div style="display: flex; align-items: center; gap: 1.5em;">
    <div style="flex: 0 0 80px;">
      <div style="width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3); position: relative;">
        <img src="images/jlu-logo.jpg" alt="Jilin University Logo" style="width: 60px; height: 60px; border-radius: 50%; object-fit: contain; background: white; padding: 8px; position: absolute;" onload="this.style.display='block';" onerror="this.style.display='none'; this.parentElement.querySelector('.fallback').style.display='flex';" />
        <div class="fallback" style="display: flex; color: white; font-weight: bold; font-size: 1.1em; align-items: center; justify-content: center; width: 100%; height: 100%; text-align: center;">JLU</div>
      </div>
    </div>
    <div style="flex: 1;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8em;">
        <h3 style="color: #2d3748; font-size: 1.3em; font-weight: 700; margin: 0; line-height: 1.2;">Undergraduate Student</h3>
        <span style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.3em 0.8em; border-radius: 20px; font-size: 0.85em; font-weight: 600;">2022.08 - Present</span>
      </div>
      <div style="color: #4a5568; font-size: 1.1em; margin-bottom: 0.5em; font-weight: 600;">
        The Second Norman Bethune Hospital, Jilin University
      </div>
      <div style="display: flex; align-items: center; gap: 1em; margin-bottom: 0.5em;">
        <span style="color: #6b7280; font-size: 0.95em;">📍 Changchun, Jilin, China</span>
        <span style="color: #6b7280; font-size: 0.95em;">🎓 Major: Clinical Medicine</span>
      </div>
    </div>
  </div>
</div>

<div style="background: linear-gradient(135deg, #fff0f6 0%, #ffffff 100%); border: 1px solid #f4c2d7; border-radius: 16px; padding: 2em; margin-bottom: 2em; box-shadow: 0 4px 20px rgba(240, 147, 251, 0.1); transition: all 0.3s ease;">
  <div style="display: flex; align-items: center; gap: 1.5em;">
    <div style="flex: 0 0 80px;">
      <div style="width: 80px; height: 80px; border-radius: 50%; background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 16px rgba(240, 147, 251, 0.3); position: relative;">
        <img src="images/nenu-logo.png" alt="Northeast Normal University Logo" style="width: 60px; height: 60px; border-radius: 50%; object-fit: contain; background: white; padding: 8px; position: absolute;" onload="this.style.display='block';" onerror="this.style.display='none'; this.parentElement.querySelector('.fallback').style.display='flex';" />
        <div class="fallback" style="display: flex; color: white; font-weight: bold; font-size: 0.9em; align-items: center; justify-content: center; width: 100%; height: 100%; text-align: center;">NENU</div>
      </div>
    </div>
    <div style="flex: 1;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8em;">
        <h3 style="color: #2d3748; font-size: 1.3em; font-weight: 700; margin: 0; line-height: 1.2;">Senior High School</h3>
        <span style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 0.3em 0.8em; border-radius: 20px; font-size: 0.85em; font-weight: 600;">2019.09 - 2022.06</span>
      </div>
      <div style="color: #4a5568; font-size: 1.1em; margin-bottom: 0.5em; font-weight: 600;">
        The High School Attached to Northeast Normal University
      </div>
      <div style="display: flex; align-items: center; gap: 1em; margin-bottom: 0.5em;">
        <span style="color: #6b7280; font-size: 0.95em;">📍 Changchun, Jilin, China</span>
        <span style="color: #6b7280; font-size: 0.95em;">🏆 Key High School</span>
      </div>
    </div>
  </div>
</div>

# 🎓 Academic Service

- **Reviewer** for MM, FedKDD WorkShop


# 🎓 Misc

- I am a big fans of Derrick Rose, Chris Bumstead and David Dai (Liang zi).
- I enjoy fitness, and my bench press max is over 100kg.
- I enjoy FPS such as CSGO, VALORANT ...
- I enjoy basketball, and have served as the starting forward for my college team.
- I enjoy hiking, and have summited Tianmenshan, Cangshan and so on.
  


<!--
# 🎡 Activities
## Academic Services
*前面的世界，以后再来探索吧*
## Invited talks (Selected)
*前面的世界，以后再来探索吧*
-->

<!--
# 🔗 Useful Links
##  🤖 Course Recommendations

- *[高等数学-兆筱小分队](https://www.bilibili.com/video/BV1dJ411c7ab/?spm_id_from=333.788&vd_source=a8a064bcbd088bc6388119f018c52df7)*

- *[线性代数-limite](https://www.bilibili.com/video/BV1L7411a7Rz/?spm_id_from=333.999.0.0&vd_source=a8a064bcbd088bc6388119f018c52df7)*

- *[Essence of linear algebra](https://www.bilibili.com/video/BV1ys411472E/?spm_id_from=333.999.0.0&vd_source=a8a064bcbd088bc6388119f018c52df7)*

- *[Linear Algebra](https://www.youtube.com/watch?v=uUrt8xgdMbs&list=PLJV_el3uVTsNmr39gwbyV-0KjULUsN7fW)*

- *[汇编语言(王爽)](https://www.bilibili.com/video/BV1Wu411B72F/?spm_id_from=333.999.0.0&vd_source=a8a064bcbd088bc6388119f018c52df7)*

- *[c语言程序设计-翁凯](https://www.icourse163.org/spoc/course/zju-121004?tid=150003#/info)*

- *[CS231n Deep Learning for Computer Vision](http://cs231n.stanford.edu/)*

## 💻 Coding Skills

- *[GIT-菜鸟教程](https://www.runoob.com/git/git-tutorial.html)*

- *[Python最佳实践指南](http://itpcb.com/docs/pythonguide/)*

- *[Pytorch入门教程-小土堆](https://www.bilibili.com/video/BV1hE411t7RN/?spm_id_from=333.999.0.0&vd_source=a8a064bcbd088bc6388119f018c52df7)*

## 🧭 Examination or Study Guides

At present, I have no time to upload all the guides. If you need more, please send me an email (of course you need attach your grade, class and name).

-  *[网安导论知识点总结](https://github.com/1NormalGuy/1normalguy.github.io/raw/main/docs/dl.pdf)*

- *[指针数组 & 数组指针 & 二级指针 辨析](https://github.com/1NormalGuy/1normalguy.github.io/raw/main/docs/points.pdf)*

- *[2023年（2024届）网安院保研打分细则](https://github.com/1NormalGuy/1normalguy.github.io/raw/main/docs/2023baoyan.pdf)*

- *[武汉大学毕业论文&实验报告latex模版-overleaf](https://cn.overleaf.com/latex/templates/tagged/whu)*

-->

<!--## 📚 Textbooks

At present, I have no time to upload all the textbooks. If you need more, please send me an email (of course you need attach your grade, class and name).

- *[高等数学（下）-武汉大学](https://github.com/1NormalGuy/1normalguy.github.io/raw/main/docs\高等数学(上).pdf)*
-->


<!--
- 计算机设计大赛经验分享, Spring 2023. \[[Slides](https://github.com/AntigoneRandy/antigonerandy.github.io/raw/main/docs/ComputerDeignCompetition.pdf)\]

- 竞赛经验漫谈, Fall 2022. \[[Slides](https://github.com/AntigoneRandy/antigonerandy.github.io/raw/main/docs/Competitions-2022Fall.pdf)\]

- 新老生经验交流会, Fall 2021. \[[Slides and Other Materials](https://github.com/AntigoneRandy/antigonerandy.github.io/raw/main/docs/ExperienceSharing2021Winter.zip)\]
-->


<!--
$^\dagger$: equal contribution, $^*$: corresponding author
-->
<!-- ## 🛰️ Geoinformatics & Remote Sensing
- [Optimized Design Method for Satellite Constellation Configuration Based on Real-time Coverage Area Evaluation](https://ieeexplore.ieee.org/document/9963835)   
Jiahao Zhou, **Boheng Li**, Qingxiang Meng   
*The 29th International Conference on Geoinformatics (CPGIS), 2022*

- [Comprehensive Evaluation of Emergency Shelters in Wuhan City Based on GIS](https://ieeexplore.ieee.org/document/9963810)   
Tingyu Luo, **Boheng Li**, Jiahao Zhou, Qingxiang Meng   
*The 29th International Conference on Geoinformatics (CPGIS), 2022* -->

<!-- ## 🤖️ AI Security, Privacy & Intellectual Property (IP) Protection -->
<!--
- [What can Discriminator do? Towards Box-free Ownership Verification of Generative Adversarial Networks](https://arxiv.org/abs/2307.15860)   
Ziheng Huang$^\dagger$, **Boheng Li**$^\dagger$, Yan Cai, Run Wang, Shangwei Guo, Liming Fang, Jing Chen, Lina Wang   
*International Conference on Computer Vision (ICCV), 2023*

- [Free Fine-tuning: A Plug-and-Play Watermarking Scheme for Deep Neural Networks](https://arxiv.org/abs/2210.07809)   
Run Wang, Jixing Ren, **Boheng Li**, Tianyi She, Wenhui Zhang, Liming Fang, Jing Chen, Lina Wang  
*ACM Multimedia (MM), 2023*

- [Dual-level Interaction for Domain Adaptive Semantic Segmentation](https://arxiv.org/abs/2307.07972)   
Dongyu Yao, **Boheng Li**$^\*$   
*ICCV Workshop on Uncertainty Quantification for Computer Vision (UnCV), 2023*


Other 2 papers regarding IP protection of DL have currently been submitted to CCF-A tier conferences.
<!-- ## 🖨️ Preprints & In Submission
-->

<!-- # 💻 Internships
To be updated. -->

<!-- # 🔗 Useful Links

## Courses

- [Linear Algebra (Hung-yi Lee, NTU, 2018)](https://www.youtube.com/watch?v=uUrt8xgdMbs&list=PLJV_el3uVTsNmr39gwbyV-0KjULUsN7fW)

- [CS229: Machine Learning](https://cs229.stanford.edu/)

- [CS230 Deep Learning](https://cs230.stanford.edu/)

- [CS231n Deep Learning for Computer Vision](http://cs231n.stanford.edu/)

- [CS224n: Natural Language Processing with Deep Learning](http://web.stanford.edu/class/cs224n/)

- [CS131 Computer Vision: Foundations and Applications](http://vision.stanford.edu/teaching/cs131_fall2223/index.html)

- [北京邮电大学鲁鹏-计算机视觉 清晰版 国家级精品课程](https://www.bilibili.com/video/BV1VW4y1v7Ph/)

- [火炉课堂-深度学习 (厦门大学)](https://www.bilibili.com/video/BV1qq4y1f7Fm)

- [中科大-凸优化](https://www.bilibili.com/video/av40868517)

- [The Next Step for Machine Learning (Hung-yi Lee, NTU, 2019)](https://www.youtube.com/watch?v=XnyM3-xtxHs&list=PLJV_el3uVTsOK_ZK5L0Iv_EQoL1JefRL4)

- [人工智能的数学基础（清华出版社）](https://www.bilibili.com/video/BV15N4y1w7e1/)

- [理解机器学习](https://www.bilibili.com/video/BV1hg411h7ys)

## Writing

- 英文学术论文写作指南 \[[link](https://www.bilibili.com/video/BV1aa411H757/)\]

- 学术规范与论文写作-南开大学程明明 \[[link](https://www.bilibili.com/video/BV18F411M7YL/)\]

- [Matplotlib cheatsheets and handouts](https://matplotlib.org/cheatsheets/)

- [十分钟掌握Seaborn，进阶Python数据可视化分析](https://zhuanlan.zhihu.com/p/49035741)

- [科学写作与哲学](https://zhuanlan.zhihu.com/p/433168083)

- [绘图软件/编程大全](https://www.bilibili.com/video/BV1gR4y1y76U)

- [如何进行高质量科研论文的写作：Shui Yu 悉尼科技大学](https://www.bilibili.com/video/BV1a8411s7Nr?p=1)

## 💻 Coding Skills

- Python最佳实践指南 \[[link](http://itpcb.com/docs/pythonguide/)\]

- Python Cookbook 3rd Edition Documentation \[[link](http://itpcb.com/docs/python3cookbook/)\]

- 🥡 Git 菜单 \[[link](http://itpcb.com/docs/gitrecipes/)\]

- Linux 基础与工具教程 \[[link](http://itpcb.com/docs/linuxtools/base/index.html)\]

## 🤖️ Artificial Intelligence & Deep Learning

- 新手如何入门pytorch？ \[[link](https://www.zhihu.com/question/55720139/answer/2788304721)\]

- 人工智能与Pytorch深度学习 \[[link](https://space.bilibili.com/100682193/channel/collectiondetail?sid=689091)\]

- [A PyTorch Tools, best practices & Styleguide](https://github.com/IgorSusmelj/pytorch-styleguide)

## Roadmap

- [科研人必看！盘点那些最好用的 AI 学术科研工具](https://zhuanlan.zhihu.com/p/153279496)

- [本科生如何自学机器学习？](https://www.zhihu.com/question/332726203/answer/737596538)

- [计算机视觉中的对抗样本 (Adversarial example)](https://zhuanlan.zhihu.com/p/352456539)

- [简单梳理一下机器学习可解释性 (Interpretability)](https://zhuanlan.zhihu.com/p/141013178)

## Misc

- [网络安全领域的科学研究和论文发表 美国西北大学 Xinyu Xing](https://www.bilibili.com/video/BV1Le4y1S7uw)

- [CVPR 9999 Best Paper——《一种加辣椒的番茄炒蛋》](https://zhuanlan.zhihu.com/p/433237905)

- [深度学习理论与实践---深度学习中的信息论：熵、最短编码、交叉熵与互信息](https://zhuanlan.zhihu.com/p/565412701)

- [Pytorch实验代码的亿些小细节](https://github.com/ahangchen/windy-afternoon/blob/master/ml/pratice/torch_best_practice.md)

- [【万字长文详解】Python库collections，让你击败99%的Pythoner](https://zhuanlan.zhihu.com/p/343747724)

- [记一次神奇的 Rebuttal 经历](https://zhuanlan.zhihu.com/p/353761920)

- [精美的终端工具 - Rich](https://www.zhihu.com/question/317758961/answer/2627662722)

- [有没有什么可以节省大量时间的 Deep Learning 效率神器？-深度学习可视化中间变量的神器Visualizer](https://www.zhihu.com/question/384519338/answer/2620414587)

- [AI-research-tools](https://github.com/bighuang624/AI-research-tools/blob/master/README.md#ai-research-tools)

- [自动超参数搜索工具optuna](https://github.com/optuna/optuna)

- [科研写作技巧](https://www.zhihu.com/question/528654768/answer/2452424449) -->
