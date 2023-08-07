#pragma once

#include "sicgl/extent.h"
#include "sicgl/screen.h"

int translate_screen_to_screen(
    screen_t* from, screen_t* to, ext_t* u, ext_t* v);
int translate_screen_to_global(screen_t* screen, ext_t* u, ext_t* v);
int translate_global_to_screen(screen_t* screen, ext_t* u, ext_t* v);
