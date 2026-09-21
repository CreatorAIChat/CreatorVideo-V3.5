# 训练路线

1. Train a licensed spatiotemporal VAE/video tokenizer.
2. Pretrain a Video DiT/flow-matching backbone on properly licensed video-text data.
3. Add image/video/audio conditioning and multimodal alignment.
4. Train identity, object, scene, camera and temporal consistency.
5. Train speech/SFX/music/audio-video synchronization and lip-sync components.
6. Train 1080p refinement and 2K/4K video super-resolution.
7. Build hierarchical long-video generation: global story -> scene -> shot -> temporal memory.
8. Run objective and human evaluation before release.

Foundation-model quality depends primarily on data, compute, training procedure and evaluation;
the toy training script is only a pipeline sanity check.
