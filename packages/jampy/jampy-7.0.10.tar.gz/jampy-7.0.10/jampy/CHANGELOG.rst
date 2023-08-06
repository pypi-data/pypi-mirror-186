Changelog
=========

V7.0.10: MC, Oxford, 17 January 2023
    - Introduced an analytic radial variation of the anisotropy ``beta``
      and ``gamma`` using a flexible logistic function of logarithmic radius
      ``beta(r) = beta_0 + (beta_inf - beta_0)/[1 + (r_a/r)^alpha]``.
      This function specifies the inner/outer anisotropy ``beta_0`` and
      ``beta_inf``, the anisotropy radius ``r_a`` and the sharpness ``alpha``
      of the transition. This new function is an alternative to assigning
      different anisotropies to different Gaussians. All procedures
      ``jam_axi_proj``, ``jam_axi_intr``, ``jam_sph_proj`` and ``jam_sph_intr``,
      with both ``align='sph'`` and ``align='cyl'``, were modified, documented
      and extensively tested to support the variable-anisotropy function.
    - ``jam_sph_proj_example``: adapted to show the usage of the new analytic
      radial anisotropy variation.
    - ``jam_axi_intr``: Fixed program stop in the plotting function.
    - ``jam_axi_proj``: Raise an error when ``rbh`` is too small.
    - ``jam_axi_proj``: Raise an error if the user includes the singularity
      ``(x,y) = (0,0)`` in the input coordinates without PSF convolution.
    - ``quad1d``: new defaults ``singular=0`` and ``epsabs=0`` like ``quad2d``.

V6.4.0: MC, Oxford, 3 October 2022
    - ``jam_sph_proj``: Created this new function by renaming the procedure
      ``legacy.jam_sph_rms`` and changing its interface to be consistent with
      the axisymmetric version.
    - ``jam_sph_proj``: Included special isotropic formula for testing.
    - ``jam_sph_proj``: Included Osipkov-Merritt anisotropy for testing.
    - ``jam_sph_proj``: Made quadrature limits insensitive to scaling.
    - ``jam_sph_proj``: Simplified integrand with formulas of Cappellari (2020)
      and using recurrence relations to reduce calls to special functions.
    - ``jam_sph_proj``: More efficient TANH transformation of the integration
      variable following Cappellari (2020).
    - ``jam_sph_intr``: New function to compute the intrinsic moments in
      spherical symmetry.
    - ``jam_axi_proj``: Removed fixed minimum radius limit in pc for the
      interpolation without PSF convolution. This avoids the risk of artificial 
      truncation when using small arbitrary spatial coordinates for testing.
    - ``jam_axi_proj``: Tenfold increase of LOS evaluations to ``nlos=1500``.
    - New procedure ``examples.jam_dark_halo_bayes_example.py``.
    - Renamed ``quadva`` as ``quad1d`` with modified interface and new
      ``singular`` keyword to skip transforming the integration variable.

V6.3.3: MC, Oxford, 7 July 2021
    - ``jam_axi_proj``: Clarified meaning of ``interp`` keyword in dosctring.     
      Thanks to Kai Zhu (nao.cas.cn) for the feedback.
    - ``jam_axi_proj``: print "No PSF/pixel convolution" when ``interp == False``.

V6.3.2: MC, Oxford, 28 April 2021
    - Use the new ``jam_axi_proj`` instead of ``legacy`` software in the examples.
    - Removed redundant ``legacy`` examples. 

V6.3.1: MC, Oxford, 11 November 2020
    - ``jam_axi_proj``: New keyword ``analytic_los`` to chose between numeric
      or analytic line-of-sight integral for the second velocity moment,
      when ``align='cyl'``.
    - ``jam_axi_proj``: Increased default value of ``nlos`` keyword.
    - ``jam_axi_proj``: Raise an error if ``rbh`` is too small.
    - ``jam_axi_proj`` and ``jam_axi_intr``: Removed ``**kwargs`` argument and
      included new ``nodots`` keyword passed to ``plot_velfield``.

V6.2.1: MC, Oxford, 15 September 2020
    - ``jam_axi_proj``: Fixed program stop when ``data == ml == None``.
      Thank to Bitao Wang (pku.edu.cn) for reporting.

V6.2.0: MC, Oxford, 17 August 2020
    - ``jam_axi_proj``: Avoid possible division by zero after convolution,
      when the tracer MGE is much smaller than the field of view.
    - ``jam_axi_proj``: Fully broadcasted ``vmom_proj``.
    - ``jam_axi_proj``: Removed minimum-radius clipping in ``vmom_proj``.
    - ``jam_axi_proj``: New ``interp`` keyword to force no-interpolation
      when using the full first and second velocity moments simultaneously.
    - Made ``jam.plot()`` callable after ``jam_axi_proj`` or ``jam_axi_intr``.
    - New axisymmetric analytic vs MGE test in ``mge_vcirc_example``.
    - ``mge_vcirc``: Upgraded formalism.
    - Fixed Numpy 1.9 ``VisibleDeprecationWarning``.
    - Updated documentation.

V6.1.5: MC, Oxford, 23 July 2020
    - Fixed program stop in first velocity moment without input data,
      introduced in V6.1.2. Thanks to Bitao Wang (pku.edu.cn) for reporting.
    - Implemented the ``kappa`` input keyword as scalar.

V6.1.4: MC, Oxford, 16 July 2020
    - Added ``kappa`` to the returned parameters of ``jam_axi_proj``.
    - Compute both velocity and Vrms in ``jam_axi_proj_example``.

V6.1.3: MC, Oxford, 13 July 2020
    - Fixed program stop in ``legacy.jam_axi_vel`` due to a variable name typo 
      introduced in V6.1.2.

V6.1.2: MC, Oxford, 20 June 2020
    - ``jam_axi_proj``: Fixed input ``ml`` being ignored. Thanks to Sabine
      Thater (univie.ac.at) and Takafumi Tsukui (grad.nao.ac.jp) for reporting.
    - ``jam_axi_rms``: I reduced the interpolation error before the PSF
      convolution for all the rotines in the ``legacy`` sub-folder, as already
      implemented in the new ``jam_axi_proj``. Thanks to Takafumi Tsukui
      (grad.nao.ac.jp) for reporting differences.
    - ``jam_axi_intr``: Request input ``data = [sigR, sigz, sigphi, vrms_phi]``
      instead of ``data = [sigR, sigz, sigphi, vphi]``.
    - ``jam_axi_intr``: exclude ``sigphi`` from ``ml`` fitting. These two
      changes make the fitted ``ml`` strictly independent of the adopted
      tangential anisotropy ``gamma``.

V6.0.1: MC, Oxford, 23 April 2020
    - Fixed ``model`` output when fitting ``ml``.
      Thanks to Selina Nitschai (mpia-hd.mpg.de) for reporting.

V6.0.0: MC, Oxford, 22 April 2020
    - Major changes to the whole ``jampy`` package: from this version
      I include the new spherically-aligned solution of the Jeans 
      equations from Cappellari (2020, MNRAS).
    - Two new functions ``jam_axi_intr`` and ``jam_axi_proj``
      now provide either the intrinsic or the projected moments,
      respectively, for both the spherically-aligned and 
      cylindrically-aligned JAM solutions.
    - I moved the previous procedures ``jam_axi_rms``, ``jam_axi_vel``
      and ``jam_sph_rms`` to the ``jampy.legacy`` folder.  

V5.0.23: MC, Oxford, 31 October 2019
    - Use analytic mge_surf in convolution.

V5.0.22: MC, Oxford, 21 March 2019
    - Reformatted documentation of all procedures.

V5.0.21: MC, Oxford, 14 February 2019
    - Significant speedup of ``mge_vcirc``.
    - Formatted documentation.
    - Created package-wide CHANGELOG: before this version, the
      CHANGELOG file only refers to the procedure ``jam_axi_rms``.

V5.0.16: MC, Oxford, 27 September 2018
    - Fixed clock DeprecationWarning in Python 3.7.

V5.0.15: MC, Oxford, 12 May 2018
    - Dropped Python 2.7 support.

V5.0.14: MC, Oxford, 17 April 2018
    - Fixed MatplotlibDeprecationWarning in Matplotlib 2.2.
    - Changed imports for jam as a package.
    - Removed example.

V5.0.13: MC, Oxford, 7 March 2018
    - Check that PSF is normalized.

V5.0.12: MC, Oxford, 22 January 2018
    - Print a message when no PSF convolution was performed.
    - Broadcast kernel and MGE convolution loops.
    - Fixed missing tensor in assertion test.

V5.0.11: MC, Oxford, 10 September 2017
    - Make default ``step`` depend on ``sigmapsf`` regardless of ``pixsize``.

V5.0.10: MC, Oxford, 10 August 2017
    - Raise an error if goodbins is all False.

V5.0.9: MC, Oxford, 17 March 2017
    - Included ``flux_obs`` keyword. Updated documentation.
    - Fixed DeprecationWarning in Numpy 1.12.

V5.0.8: MC, Oxford, 17 February 2017
    - Use odd kernel size for convolution.
    - Fixed corner case with coordinates falling outside the 
      interpolation region, due to finite machine precision.

V5.0.7: MC, Oxford, 23 February 2016
    - Scale rmsModel by the input M/L also when rms is not given.
      Thanks to Alex Grainger (Oxford) for pointing out the inconsistency.
    - Pass ``**kwargs`` for plotting.

V5.0.6: MC, Oxford, 18 September 2015
    - Plot bad bins on the data.

V5.0.5: MC, Oxford, 23 May 2015
    - Changed meaning of goodbins to be a boolean vector.

V5.0.4: MC, Sydney, 5 February 2015
    - Introduced further checks on matching input sizes.

V5.0.3: MC, Oxford, 31 October 2014
    - Modified final plot layout.

V5.0.2: MC, Oxford, 25 May 2014
    - Support both Python 2.7 and Python 3.

V5.0.1: MC, Oxford, 24 February 2014
    - Plot bi-symmetrized V_rms as in IDL version.

V5.0.0: MC, Paranal, 11 November 2013
    - Translated from IDL into Python.

V4.1.5: MC, Paranal, 8 November 2013
    - Use renamed CAP_* routines to avoid potential naming conflicts.

V4.1.4: MC, Oxford, 12 February 2013
    - Include _EXTRA and RANGE keywords for plotting.

V4.1.3: MC, Oxford, 1 February 2013
    - Output FLUX in Lsun/pc^2.

V4.1.2: MC, Oxford, 28 May 2012
    - Updated documentation.

V4.1.1: MC, Oxford, 8 December 2011
    - Only calculates FLUX if required.

V4.1.0: MC, Oxford 19 October 2010
    - Included TENSOR keyword to calculate any of the six components of
      the symmetric proper motion dispersion tensor (as in note 5 of the paper).

V4.0.9: MC, Oxford, 15 September 2010
    - Plot and output with FLUX keyword the PSF-convolved MGE surface brightness.

V4.0.8: MC, Oxford, 09 August 2010
    - Use linear instead of smooth interpolation. After feedback from Eric Emsellem.

V4.0.7: MC, Oxford, 01 March 2010
    - Forces q_lum && q_pot < 1.

V4.0.6: MC, Oxford, 08 February 2010
    - The routine TEST_JAM_AXISYMMETRIC_RMS with the usage example now adopts a
      more realistic input kinematics.
    - Updated documentation.

V4.0.5: MC, Oxford, 6 July 2009
    - Skip unnecessary interpolation when computing a few points without PSF
      convolution. After feedback from Eric Emsellem.

V4.0.4: MC, Oxford, 29 May 2009
    - Compute FLUX even when not plotting.

V4.0.3: MC, Oxford 4 April 2009
    - Added keyword RBH.

V4.0.2: MC, Oxford, 21 November 2008
    - Added keywords NRAD and NANG. Thanks to Michael Williams for
      reporting possible problems with too coarse interpolation.

V4.0.1: MC, Windhoek, 29 September 2008
    - Bug fix: when ERMS was not given, the default was not properly set.
      Included keyword STEP. The keyword FLUX is now only used for output:
      the surface brightness for plotting is computed from the MGE model.

V4.0.0: MC, Oxford, 11 September 2008
    - Implemented PSF convolution using interpolation on a polar grid.
      Dramatic speed-up of calculation. Further documentation.

V3.2.0: MC, Oxford, 14 August 2008
    - Updated documentation.

V3.1.3: MC, Oxford, 12 August 2008
    - First released version.

V2.0.0: MC, Oxford, 20 September 2007
    - Introduced new solution of the MGE Jeans equations with constant
      anisotropy sig_R = b*sig_z.

V1.0.0: Michele Cappellari, Vicenza, 19 November 2003
    - Written and tested
