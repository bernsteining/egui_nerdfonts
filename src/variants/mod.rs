pub mod regular;

#[derive(Debug, Clone, Copy)]
pub enum Variant {
    Regular,
}

impl Variant {
    pub fn font_data(&self) -> egui::FontData {
        let mut font_data =
            egui::FontData::from_static(include_bytes!("../../fonts/nerdfonts_regular.ttf"));
        font_data.tweak.y_offset_factor = 0.0;
        font_data
    }
}
