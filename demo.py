from pil_resize_aspect_ratio import Resizer, FillType

p_org_img_bg  = 'bg.png'
p_overlay_img = 'fg.png'
path_out = 'final.png'

resized_bg_image = Resizer.resize_keep_aspect_ratio(
    image=p_org_img_bg,
    fill_type=FillType.Fill,
    target_size=(1920, 1080),
    return_image_instead_of_success=False
)

print(
    Resizer.paste_and_fit(
        background_image=resized_bg_image,
        foreground_image=p_overlay_img,
        path_out=path_out
    )
)