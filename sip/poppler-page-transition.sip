namespace Poppler {

class PageTransition {
%TypeHeaderCode
#include <qt5/poppler-qt5.h>
#include <qt5/poppler-page-transition.h>
%End

public:

    enum Type {
        Replace = 0,
        Split,
        Blinds,
        Box,
        Wipe,
        Dissolve,
        Glitter,
        Fly,
        Push,
        Cover,
        Uncover,
        Fade,
    };
    enum Alignment {
        Horizontal = 0,
        Vertical,
    };

    enum Direction {
        Inward = 0,
        Outward,
    };
    //   PageTransition(const PageTransitionParams &params);
    PageTransition(const Poppler::PageTransition &pt);
    ~PageTransition();
    Type type() const;
%If(POPPLER_V0_20_0 - POPPLER_V0_36_0)
    double durationReal() const;
%End
%If(POPPLER_V0_36_0 - )
    Alignment alignment() const;
%End
    Direction direction() const;
    int angle() const;
    double scale() const;
    bool isRectangular() const;
}; // class PageTransition


}; // namespace Poppler

/* kate: indent-width 4; space-indent on; hl c++; indent-mode cstyle; */
