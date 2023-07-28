fn main() {
    eframe::run_native(
        "egui_nerdfonts demo",
        eframe::NativeOptions {
            initial_window_size: Some(egui::vec2(320.0, 755.0)),
            ..Default::default()
        },
        Box::new(|cc| Box::new(Demo::new(cc))),
    )
    .unwrap();
}

struct Demo {}

impl Demo {
    fn new(cc: &eframe::CreationContext) -> Self {
        let mut fonts = egui::FontDefinitions::default();

        egui_nerdfonts::add_to_fonts(&mut fonts, egui_nerdfonts::Variant::Regular);

        cc.egui_ctx.set_fonts(fonts);

        Self {}
    }
}

impl eframe::App for Demo {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            egui::Frame::canvas(ui.style()).show(ui, |ui| {
                ui.label(
                    egui::RichText::new(format!(
                        "egui_nerdfonts::regular::LANGUAGE_RUST: {}",
                        egui_nerdfonts::regular::LANGUAGE_RUST
                    ))
                        .size(42.),
                );
            });
        });
    }
}
