#include "imgui.h"
#include "hello_imgui/hello_imgui.h"
#include "immapp/immapp.h"
#include "hello_imgui/icons_font_awesome.h"
#include "demo_utils/api_demos.h"
#include "hello_imgui/hello_imgui_include_opengl.h"

void LoadFonts()
{
    // load a lot of fonts, to trigger the issue
    //for (float fontSize = 14.f; fontSize < 150.f; fontSize += 1.f)
    //ImGui::GetIO().Fonts->AddFontFromFileTTF("demos_assets/fonts/DroidSans.ttf", 655); // any font file will do
    HelloImGui::LoadFontTTF("fonts/DroidSans.ttf", 329.f);
}

void Gui()
{
    bool b = ImGui::GetIO().Fonts->IsBuilt(); // will return true even if the fonts build failed!

    auto error = glGetError();

    // This will not render correctly when the build failed
    // (However CalcTextSize still returns coherent values)
    ImGui::Text("Hello, world!");
}


int main(int, char**)
{
    ChdirBesideAssetsFolder();

    HelloImGui::RunnerParams runnerParams;
    runnerParams.callbacks.LoadAdditionalFonts = LoadFonts;
    runnerParams.callbacks.ShowGui = Gui;

    ImmApp::Run(runnerParams);
    return 0;
}