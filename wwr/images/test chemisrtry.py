<!DOCTYPE html>
<!-- saved from url=(0189)https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13#diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R1-R254 -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  
  
  
  
  
  

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./test chemisrtry_files/light-efd2f2257c96.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./test chemisrtry_files/dark-6b1e37da2254.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-aa16bfa90fb8.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-f4daad25d8cf.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-a4629b2e906b.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-afcc3a6a38dd.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-79bca7145393.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-fe4137b54b26.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-1911f0cf0db4.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./test chemisrtry_files/primer-primitives-8500c2c7ce5f.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./test chemisrtry_files/primer-61560ce103d3.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./test chemisrtry_files/global-526475a50099.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./test chemisrtry_files/github-0c7b5281bcc9.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./test chemisrtry_files/repository-7247b57543b3.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./test chemisrtry_files/code-68246ade0881.css">

  


  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["code_vulnerability_scanning","copilot_chat_static_thread_suggestions","copilot_chat_dotcom_user_server_tokens","copilot_conversational_ux_history_refs","copilot_followup_to_agent","copilot_smell_icebreaker_ux","copilot_implicit_context","copilot_stop_response","failbot_handle_non_errors","geojson_azure_maps","ghost_pilot_vnext","marketing_forms_api_integration_contact_request","marketing_pages_search_explore_provider","repository_suggester_elastic_search","turbo_experiment_risky","sample_network_conn_type","no_character_key_shortcuts_in_inputs","react_start_transition_for_navigations","custom_inp","remove_child_patch","nested_list_view_dnd","kb_source_repos","filter_prefetch_suggestions"]}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/wp-runtime-fd59e65a3e44.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_dompurify_dist_purify_js-810e4b1b9abd.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover_js-4ac41d0a76fd.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_smoothscroll-polyfill_di-75db2e-e091a6d939e9.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/environment-a36e9a1c67ad.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-03bcda509ec9.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-9f960d9b217c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_details-d-ed9a97-dfdebffa4a55.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_text-expander-element_dist_index_js-b2135edb5ced.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_delegated-events_dist_in-3efda3-bd1c71f99e25.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-b7d8f4-6e6f83bcc978.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_clipboard-copy-element_-782ca5-14181f295dc0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-c238a4-a49e223f0ca2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/app_assets_modules_github_onfocus_ts-ui_packages_trusted-types-policies_policy_ts-ui_packages-6fe316-d97d91568d25.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/github-elements-a67805df382e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/element-registry-91d3d26e0e37.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-4da1df-b779d50bdb3a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_braintree_browser-detection_dist_browser-detection_js-node_modules_stack-68835d-59206c834a41.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_lit-html_lit-html_js-cc7cb714ead5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_morphdom_dist_morphdom-e-7c534c-38ef9cb819da.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-1cea0f5eff45.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-893f9f-880ac2bbb719.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_scroll-anchoring_dist_scroll-anchoring_esm_js-node_modules_github_hotkey-1a1d91-56e858031112.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_color-convert_index_js-cdd1e82b3795.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_jtml_lib_index_js-b1947a1d4855.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-da6ec6-77ce2f267f4e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_textarea-autosi-9e0349-7c78ee755ad3.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/app_assets_modules_github_updatable-content_ts-fd68b41b03a0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_onfocus_ts-app_ass-421cec-4a1d8a9ad687.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/app_assets_modules_github_sticky-scroll-into-view_ts-4dd22d959621.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-467754-acdbd37f0cc6.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-26fa06a2383b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/app_assets_modules_github_blob-anchor_ts-app_assets_modules_github_filter-sort_ts-app_assets_-c96432-a9a6d17d145c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/behaviors-ac844bd01e4d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-06ff531-2ea61fcc9a71.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/notifications-global-ce1721184096.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_catalyst_lib_inde-dbbea9-bac2d7b04358.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/app_assets_modules_github_repositories_get-repo-element_ts-6258973fbfd5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/code-menu-14f80622cb85.js.download"></script>
  
  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/react-lib-a89cbd87a1e0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_primer_octicons-react_di-b40d97-9b98c5140e22.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_Box_Box_js-5a335cbe71ad.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_Button_Button_js-83e3876ae2f4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_TooltipV2_Tooltip_js-bf3e8e618a5c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_clsx_dist_clsx_m_js-node_modules_primer_react_node_modules_primer_octico-c56103-69406d13de9c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-71451907bb28.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_Text_Text_js-node_modules_primer_react_lib-esm_Text-7845da-072b25840dd1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_ActionMenu_ActionMenu_js-node_modules_primer_react_-5b2420-de3627095d51.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_FormControl_FormControl_js-31b7ef432e82.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_react-router-dom_dist_index_js-b2efb8a73d21.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_Link_Link_js-node_modules_primer_react_lib-esm_Rela-a903d7-902695cc4f67.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_ConfirmationDialog_ConfirmationDialog_js-7dd1f3d921fe.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_Heading_Heading_js-node_modules_primer_react_lib-es-20c766-54e9a847a531.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_TreeView_TreeView_js-9ffa476c9975.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_FeatureFlags_FeatureFlags_js-node_modules_primer_re-12c85c-366acf315a92.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_Avatar_Avatar_js-node_modules_primer_react_lib-esm_-626be3-7dbdbcd4fbf6.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_Button_LinkButton_js-node_modules_primer_react_lib--039852-fd29b8fce349.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/ui_packages_react-core_create-browser-history_ts-ui_packages_safe-storage_safe-storage_ts-ui_-682c2c-d91aaa72a6fc.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/ui_packages_react-core_register-app_ts-2b821810213c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/ui_packages_paths_index_ts-ff418cbe4280.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/ui_packages_ref-selector_RefSelector_tsx-52da906e4fee.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/ui_packages_commit-attribution_index_ts-ui_packages_commit-checks-status_index_ts-ui_packages-f45efb-6e916c8dcaa1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/ui_packages_code-view-shared_hooks_use-canonical-object_ts-ui_packages_code-view-shared_hooks-af4274-ec84d86a2bde.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/ui_packages_code-view-shared_components_files-search_FileResultsList_tsx-0d7fc8af4be4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/ui_packages_code-view-shared_hooks_use-file-page-payload_ts-ui_packages_code-view-shared_util-337bac-9d3a5c01250f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/ui_packages_repos-file-tree-view_repos-file-tree-view_ts-ui_packages_react-core_JsonRoute_tsx-de5e5348c6da.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/react-code-view-3c77650e9f4d.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./test chemisrtry_files/react-code-view.234ae39ff1fa1232236c.module.css">


  



  
  
  

    
  


  


    


  
  

  
  

    



  

  




    

  

    

    

      

      

    
    
    

      
  
  


      
      


      


      

        


  <meta http-equiv="x-pjax-version" content="5ccb8459dc437e11e0b978d192ccd7f038e709a42fe7cac8677e8338094efc38" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="f6e41c3092c5e1167d95330a2a482f695598c31ad79963c59b07ab79dbfb87f7" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="597a55ac25fc4ca4d5fcba33bbd88f3b1fc47ace41e89daf394f76b0841d0979" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="917a3faab0a2dbe29b817ac86a66cebbdced06421b579fd5bec2e62df3ecf68a" data-turbo-track="reload">

  

      
    
  

  



    

    


  

  

  
  
  





  

  <style data-styled="active" data-styled-version="5.3.6"></style><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><link crossorigin="anonymous" media="all" rel="stylesheet" href="./test chemisrtry_files/notifications-subscriptions-menu.572fff1cb5c3caef1ac9.module.css"><script type="application/json" id="client-env">{"locale":"en","featureFlags":["code_vulnerability_scanning","copilot_chat_static_thread_suggestions","copilot_chat_dotcom_user_server_tokens","copilot_conversational_ux_history_refs","copilot_followup_to_agent","copilot_smell_icebreaker_ux","copilot_implicit_context","copilot_stop_response","failbot_handle_non_errors","geojson_azure_maps","ghost_pilot_vnext","marketing_forms_api_integration_contact_request","marketing_pages_search_explore_provider","repository_suggester_elastic_search","turbo_experiment_risky","sample_network_conn_type","no_character_key_shortcuts_in_inputs","react_start_transition_for_navigations","report_hydro_web_vitals","custom_inp","remove_child_patch","nested_list_view_dnd","kb_source_repos","filter_prefetch_suggestions"]}</script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_index_js-878844713bc9.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-e53a3f-52039a64560e.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/app_assets_modules_github_ref-selector_ts-75a3ab0a8783.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/codespaces-db45f047ba18.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-5b684a-3637aaaec00b.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_mini-th-9dbbd2-d7a3fae24e68.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/repositories-ff512d343c0e.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_SelectPanel_SelectPanel_js-84ec020d6084.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/notifications-subscriptions-menu-7b23edb1862e.js.download"></script><style type="text/css" id="ms-consent-banner-theme-styles"></style><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-b353f7-c443d0101ada.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_scroll-anchoring_di-087b76-ec5e1d1ea401.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/app_assets_modules_github_diffs_blob-lines_ts-app_assets_modules_github_diffs_linkable-line-n-d80317-233693f91d25.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/diffs-2ffc0643f851.js.download"></script><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>chemistry · mattfelber/CSE-111-programming-with-functions@9515ecf</title><meta name="route-pattern" content="/_view_fragments/Voltron::CommitFragmentsController/show/:user_id/:repository/:name/repo_layout(.:format)" data-turbo-transient=""><meta name="route-controller" content="voltron_commit_fragments" data-turbo-transient=""><meta name="route-action" content="repo_layout" data-turbo-transient=""><meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb"><meta name="request-id" content="60AF:3AB413:22AC632:2384811:668A013E" data-turbo-transient="true"><meta name="html-safe-nonce" content="49cea44089d658e703c1a33128f111ea2992885e14d6368ddee77c85caf63873" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9tYXR0ZmVsYmVyL0NTRS0xMTEtcHJvZ3JhbW1pbmctd2l0aC1mdW5jdGlvbnMvdHJlZS9tYWluIiwicmVxdWVzdF9pZCI6IjYwQUY6M0FCNDEzOjIyQUM2MzI6MjM4NDgxMTo2NjhBMDEzRSIsInZpc2l0b3JfaWQiOiI2NTQ1OTgxMDM3ODk4NjI2MTkxIiwicmVnaW9uX2VkZ2UiOiJmcmEiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-turbo-transient="true"><meta name="visitor-hmac" content="74df0ac06f5d3e2ffe22f832ab6df4c43d6a14bfb5d0f3d151be7bfca063a32e" data-turbo-transient="true"><meta name="hovercard-subject-tag" content="repository:713670672" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,commits,copilot" data-turbo-transient="true"><meta name="selected-link" value="repo_commits" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="172101276"><meta name="octolytics-actor-login" content="emmanuel2011-program"><meta name="octolytics-actor-hash" content="2ee90c64f9fcbe7b2b970f80065cbde37b95eafbccabe117eb20ebd7fa58abeb"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/voltron/commit_fragments/repo_layout" data-turbo-transient="true"><meta name="user-login" content="emmanuel2011-program"><link rel="sudo-modal" href="https://github.com/sessions/sudo_modal"><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><link href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13.diff" rel="alternate" type="text/plain+diff" data-turbo-transient="true"><link href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13.patch" rel="alternate" type="text/plain+patch" data-turbo-transient="true"><meta name="diff-view" content="unified" data-turbo-transient=""><meta name="voltron-timing" value="328"><meta name="go-import" content="github.com/mattfelber/CSE-111-programming-with-functions git https://github.com/mattfelber/CSE-111-programming-with-functions.git"><meta name="octolytics-dimension-user_id" content="111910246"><meta name="octolytics-dimension-user_login" content="mattfelber"><meta name="octolytics-dimension-repository_id" content="713670672"><meta name="octolytics-dimension-repository_nwo" content="mattfelber/CSE-111-programming-with-functions"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="713670672"><meta name="octolytics-dimension-repository_network_root_nwo" content="mattfelber/CSE-111-programming-with-functions"><meta name="turbo-body-classes" content="logged-in env-production page-responsive"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><style type="text/css" id="ms-consent-banner-theme-styles"></style></head>

  <body class="logged-in env-production page-responsive full-width" style="overflow-wrap: break-word; --dialog-scrollgutter: 17px;">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative js-header-wrapper ">
      <a href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13#start-of-content" data-skip-target-assigned="false" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/react-lib-a89cbd87a1e0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_primer_octicons-react_di-b40d97-9b98c5140e22.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_Box_Box_js-5a335cbe71ad.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_Button_Button_js-83e3876ae2f4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_TooltipV2_Tooltip_js-bf3e8e618a5c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_clsx_dist_clsx_m_js-node_modules_primer_react_node_modules_primer_octico-c56103-69406d13de9c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-71451907bb28.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_Dialog_Dialog_js-node_modules_primer_react_lib-esm_-af9f6c-cebcdb5fbc77.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/ui_packages_react-core_create-browser-history_ts-ui_packages_safe-storage_safe-storage_ts-ui_-682c2c-d91aaa72a6fc.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/keyboard-shortcuts-dialog-f6d4ee842c1e.js.download"></script>

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r31:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>




      

        

            <header class="AppHeader" role="banner">
  <h2 class="sr-only">Navigation Menu</h2>

    

    <div class="AppHeader-globalBar pb-2 js-global-bar">
      <div class="AppHeader-globalBar-start">
          <deferred-side-panel data-url="/_side-panels/global" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-daa850d8-106d-4960-9843-f5f38360174f" id="dialog-show-dialog-daa850d8-106d-4960-9843-f5f38360174f" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-bg-transparent p-0 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>

<dialog-helper>
  <dialog data-target="deferred-side-panel.panel" id="dialog-daa850d8-106d-4960-9843-f5f38360174f" aria-modal="true" aria-labelledby="dialog-daa850d8-106d-4960-9843-f5f38360174f-title" aria-describedby="dialog-daa850d8-106d-4960-9843-f5f38360174f-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade Overlay--placement-left SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-daa850d8-106d-4960-9843-f5f38360174f-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-daa850d8-106d-4960-9843-f5f38360174f" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="dialog-daa850d8-106d-4960-9843-f5f38360174f-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-target="nav-list.topLevelList" data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g d" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;HOME&quot;,&quot;label&quot;:null}" id="item-e46726b7-eec3-4b90-8251-f411fb383fc7" href="https://github.com/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span></a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES&quot;,&quot;label&quot;:null}" id="item-a8d84921-8c5a-4736-b836-fef7d67dc059" href="https://github.com/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span></a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS&quot;,&quot;label&quot;:null}" id="item-ce14e8f1-e23b-45b1-9149-007a4026e6fa" href="https://github.com/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROJECTS&quot;,&quot;label&quot;:null}" id="item-3d6b78ec-3be1-4af9-95f1-4509cd5e5647" href="https://github.com/projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span></a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DISCUSSIONS&quot;,&quot;label&quot;:null}" id="item-f675bd7a-34da-4764-8705-71ef54f7953b" href="https://github.com/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span></a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;CODESPACES&quot;,&quot;label&quot;:null}" id="item-1fca6969-4c5c-4f46-a87d-2c5886987914" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Codespaces
</span></a>
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;EXPLORE&quot;,&quot;label&quot;:null}" id="item-f26bf6f1-555e-4ac4-a97b-056ac7c5c808" href="https://github.com/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span></a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MARKETPLACE&quot;,&quot;label&quot;:null}" id="item-46ea25b8-b88d-4ef0-814c-de2a6636797d" href="https://github.com/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span></a>
  
</li>

</ul>  </nav-list>
</nav>

        <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
          <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>  <span class="sr-only">Loading</span>

</div>
</div>
      <div data-view-component="true" class="flex-1"></div>


      <div data-view-component="true" class="px-2">      <p class="color-fg-subtle text-small text-light">© 2024 GitHub, Inc.</p>

      <div data-view-component="true" class="d-flex flex-wrap text-small text-light">
          <a target="_blank" href="https://github.com/about" data-view-component="true" class="Link mr-2">About</a>
          <a target="_blank" href="https://github.blog/" data-view-component="true" class="Link mr-2">Blog</a>
          <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link mr-2">Terms</a>
          <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link mr-2">Privacy</a>
          <a target="_blank" href="https://github.com/security" data-view-component="true" class="Link mr-2">Security</a>
          <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="Link mr-3">Status</a>

</div></div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>

  </include-fragment>
</deferred-side-panel>

        <a class="AppHeader-logo ml-2" href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
          <svg height="32" aria-hidden="true" viewBox="0 0 16 16" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
        </a>

          <div class="AppHeader-context">
  <div class="AppHeader-context-compact">
      <button aria-expanded="false" aria-haspopup="dialog" aria-label="Page context: mattfelber / CSE-111-programming-with-functions" id="dialog-show-context-region-dialog" data-show-dialog-id="context-region-dialog" type="button" data-view-component="true" class="AppHeader-context-compact-trigger Truncate Button--secondary Button--medium Button box-shadow-none">  <span class="Button-content">
    <span class="Button-label"><span class="AppHeader-context-compact-lead">
                <span class="AppHeader-context-compact-parentItem">mattfelber</span>
                <span class="no-wrap">&nbsp;/</span>

            </span>

            <strong class="AppHeader-context-compact-mainItem d-flex flex-items-center Truncate">
  <span class="Truncate-text ">CSE-111-programming-with-functions</span>

</strong></span>
  </span>
</button>

<dialog-helper>
  <dialog id="context-region-dialog" aria-modal="true" aria-labelledby="context-region-dialog-title" aria-describedby="context-region-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="context-region-dialog-title">
        Navigate back to
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="context-region-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="context-region-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">          <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;mattfelber&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/mattfelber" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-person mr-1">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>

          mattfelber
        </span>

</a>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;CSE-111-programming-with-functions&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/mattfelber/CSE-111-programming-with-functions" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-repo mr-1">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>

          CSE-111-programming-with-functions
        </span>

</a>
    </li>
</ul>

</div>
      </scrollable-region>
      
</dialog></dialog-helper>
  </div>

  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="Page context">
      <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;mattfelber&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/mattfelber/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/mattfelber" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          mattfelber
        </span>

</a>
        <span class="AppHeader-context-item-separator">/</span>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;CSE-111-programming-with-functions&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="https://github.com/mattfelber/CSE-111-programming-with-functions" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          CSE-111-programming-with-functions
        </span>

</a>
    </li>
</ul>

    </nav>
  </div>
</div>

      </div>
      <div class="AppHeader-globalBar-end">
          <div class="AppHeader-search">
              


<qbsearch-input class="search-input" data-scope="repo:mattfelber/CSE-111-programming-with-functions" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="qZ5HXvimLsu3V3MDUrzA2WASTw-gV0FmMrdnA7sjRMnOXiqmKN_IbA_HC_DrgkzlsxTWWasCChnAmr32Tz76Sg" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="mattfelber/CSE-111-programming-with-functions" data-current-org="" data-current-owner="mattfelber" data-logged-in="true" data-copilot-chat-enabled="false" data-blackbird-indexed-repo-csrf="&lt;input type=&quot;hidden&quot; value=&quot;WeBHKdSp_l_JY4azq8S8Rdo5tUhmyRV22G09otwo7_qOozgdYXcQyCQRn_j-twitqBYB-4y23WFRXdoNBc7j7Q&quot; data-csrf=&quot;true&quot; /&gt;" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control">
      <label for="AppHeader-searchInput" aria-label="Search or jump to…" class="AppHeader-search-visual--leading">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button type="button" data-target="qbsearch-input.inputButton" data-action="click:qbsearch-input#handleExpand" class="AppHeader-searchButton form-control input-contrast text-left color-fg-subtle no-wrap placeholder" data-hotkey="s,/" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;SEARCH&quot;,&quot;label&quot;:null}" aria-describedby="search-error-message-flash">
            <div class="overflow-hidden">
              <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
              </span>
            </div>
          </button>

    </div>


  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-40b5f5fe-910e-4d40-a580-4fc547f54a4a" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-40b5f5fe-910e-4d40-a580-4fc547f54a4a" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">
              Search syntax tips
</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="jQz85z2KiSn9X5_6dJFRB2tDTrYenAe5QpnxnKtWJ38GLsb2_xMEyL6vJrQRtLXBNqQI1bRXE3Axo4g67C08eg">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="VM3kCx9dQ6D1Zei0YxgpYNwUnIDZcOUsDah1Z9eNB1pP6V_bhm2iqpH-rHYuJSGntr3QJJu6P37v8YNyDpuZyw">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="l2KS3DEypvA6F5NK9wZpfEkMbUWPupeUrXEZi4hosfXvcnfUKkW3V37B7LTpn3j2kPYdLFM7FYQAW_BQ_urzrw" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input><input type="hidden" value="rfZNIV8Gl_s57kSDUXHWQDufLfj6vEWatrbvC2aKvdNThHkAsqEirocP-P59jGxyjeEVuoT-5aOqVlfISsOvXA" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">

          </div>

        <div class="AppHeader-actions position-relative">
             <react-partial-anchor data-catalyst="">
      <button id="global-create-menu-anchor" aria-label="Create something new" data-target="react-partial-anchor.anchor" type="button" data-view-component="true" class="AppHeader-button global-create-button Button--secondary Button--medium Button width-auto color-fg-muted" aria-describedby="tooltip-30641968-32cd-452c-8ada-684da3709407" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-30641968-32cd-452c-8ada-684da3709407" for="global-create-menu-anchor" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Create new...</tool-tip>

      
    
        






<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_ActionMenu_ActionMenu_js-node_modules_primer_react_-5b2420-de3627095d51.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/vendors-node_modules_primer_react_lib-esm_FeatureFlags_FeatureFlags_js-node_modules_primer_re-d6531f-657a261479d0.js.download"></script>

<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/ui_packages_react-core_register-partial_ts-ui_packages_global-create-menu_GlobalCreateMenu_tsx-7eb14e316154.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/global-create-menu-7261cfc312b8.js.download"></script>

<react-partial partial-name="global-create-menu" data-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"createRepo":true,"importRepo":true,"codespaces":true,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/emmanuel2011-program?tab=projects","createLegacyProject":false,"createIssue":false,"org":null,"owner":"mattfelber","repo":"CSE-111-programming-with-functions"}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r32:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>

      </react-partial-anchor>


          <a href="https://github.com/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-077964d6-6fd9-4404-b6e0-43252dffd95e" aria-labelledby="tooltip-abbb9bb7-e3e4-44ff-9f00-c4d08cd34e18" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a><tool-tip id="tooltip-abbb9bb7-e3e4-44ff-9f00-c4d08cd34e18" for="icon-button-077964d6-6fd9-4404-b6e0-43252dffd95e" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Issues</tool-tip>

          <a href="https://github.com/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-a0dbfa40-5c25-4894-84fd-7e67a98d6bf8" aria-labelledby="tooltip-df1105c4-3cbd-4367-bfbd-a17c42cdc9b5" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-df1105c4-3cbd-4367-bfbd-a17c42cdc9b5" for="icon-button-a0dbfa40-5c25-4894-84fd-7e67a98d6bf8" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Pull requests</tool-tip>

        </div>

        <notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTcyMTAxMjc2IiwidCI6MTcyMDMyMDM0NX0=--d4c5fdbb0bfe52899874f7cac10fcd742acd87950786e05cc6fcdf81ca66ef3c" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel" data-fetch-retry-delay-time="500" data-catalyst="">
    <a id="AppHeader-notifications-button" href="https://github.com/notifications" aria-labelledby="notification-indicator-tooltip" data-hotkey="g n" data-target="notification-indicator.link" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;NOTIFICATIONS_HEADER&quot;,&quot;label&quot;:&quot;icon:read&quot;}" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox Button-visual">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</a>

    <tool-tip id="notification-indicator-tooltip" data-target="notification-indicator.tooltip" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>You have no unread notifications</tool-tip>
</notification-indicator>

        

        <div class="AppHeader-user">
          <deferred-side-panel data-url="/_side-panels/user?react_global_nav=true&amp;repository_id=713670672" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <react-partial-anchor data-catalyst="">
    <button data-target="react-partial-anchor.anchor" data-login="emmanuel2011-program" aria-label="Open user navigation menu" type="button" data-view-component="true" class="Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
    <span class="Button-label"><img src="./test chemisrtry_files/172101276" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle"></span>
  </span>
</button>
    
  
      










<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./test chemisrtry_files/global-user-nav-drawer-7e60575a7bd9.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./test chemisrtry_files/global-user-nav-drawer.c80e6513685ad96a3f54.module.css">

<react-partial partial-name="global-user-nav-drawer" data-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"owner":{"login":"emmanuel2011-program","name":"emmyo","avatarUrl":"https://avatars.githubusercontent.com/u/172101276?v=4"},"drawerId":"global-user-nav-drawer","lazyLoadItemDataFetchUrl":"/_side-panels/user.json","addAccountPath":"/login?add_account=1\u0026return_to=https%3A%2F%2Fgithub.com%2Fmattfelber%2FCSE-111-programming-with-functions%2Fcommit%2F9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13","switchAccountPath":"/switch_account","loginAccountPath":"/login?add_account=1","projectsPath":"/emmanuel2011-program?tab=projects","gistsUrl":"https://gist.github.com/mine","docsUrl":"https://docs.github.com","yourEnterpriseUrl":null,"enterpriseSettingsUrl":null,"supportUrl":"https://support.github.com","showAccountSwitcher":true,"showEnterprises":true,"showEnterprise":false,"showGists":true,"showSponsors":true,"showFeaturesPreviews":true,"showEnterpriseSettings":false,"createMenuProps":{"createRepo":true,"importRepo":true,"codespaces":true,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/emmanuel2011-program?tab=projects","createLegacyProject":false,"createIssue":false,"org":null,"owner":"mattfelber","repo":"CSE-111-programming-with-functions"}}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r35:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>

    </react-partial-anchor>

  </include-fragment>
</deferred-side-panel>
        </div>

        <div class="position-absolute mt-2">
            
<site-header-logged-in-user-menu data-catalyst="">

</site-header-logged-in-user-menu>

        </div>
      </div>
    </div>


      <div class="AppHeader-localBar">
        <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/mattfelber/CSE-111-programming-with-functions" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /mattfelber/CSE-111-programming-with-functions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected" aria-current="page">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/mattfelber/CSE-111-programming-with-functions/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /mattfelber/CSE-111-programming-with-functions/issues /_view_fragments/issues/index/mattfelber/CSE-111-programming-with-functions/layout" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/mattfelber/CSE-111-programming-with-functions/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /mattfelber/CSE-111-programming-with-functions/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/mattfelber/CSE-111-programming-with-functions/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /mattfelber/CSE-111-programming-with-functions/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/mattfelber/CSE-111-programming-with-functions/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /mattfelber/CSE-111-programming-with-functions/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/mattfelber/CSE-111-programming-with-functions/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /mattfelber/CSE-111-programming-with-functions/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/mattfelber/CSE-111-programming-with-functions/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /mattfelber/CSE-111-programming-with-functions/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-593d8289-232d-4909-968f-ee2b963d09cc-button" popovertarget="action-menu-593d8289-232d-4909-968f-ee2b963d09cc-overlay" aria-controls="action-menu-593d8289-232d-4909-968f-ee2b963d09cc-list" aria-haspopup="true" aria-labelledby="tooltip-6cdb113c-386a-42a1-8fbd-a892acfb68f7" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-6cdb113c-386a-42a1-8fbd-a892acfb68f7" for="action-menu-593d8289-232d-4909-968f-ee2b963d09cc-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position id="action-menu-593d8289-232d-4909-968f-ee2b963d09cc-overlay" anchor="action-menu-593d8289-232d-4909-968f-ee2b963d09cc-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-593d8289-232d-4909-968f-ee2b963d09cc-button" id="action-menu-593d8289-232d-4909-968f-ee2b963d09cc-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-e5d1862c-483f-4a56-84b7-dc2eaec5cf74" href="https://github.com/mattfelber/CSE-111-programming-with-functions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span></a>
  
</li>
        <li hidden="" data-menu-item="i1issues-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-50c00e4a-40f7-4b06-9c90-313cc72b1d28" href="https://github.com/mattfelber/CSE-111-programming-with-functions/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span></a>
  
</li>
        <li hidden="" data-menu-item="i2pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-7554a5a5-9fc2-408e-99ed-23defe1d9f4f" href="https://github.com/mattfelber/CSE-111-programming-with-functions/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span></a>
  
</li>
        <li hidden="" data-menu-item="i3actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-79a9aea2-dfb3-48d3-91cf-ef96e01b696e" href="https://github.com/mattfelber/CSE-111-programming-with-functions/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span></a>
  
</li>
        <li hidden="" data-menu-item="i4projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-b24d620a-fc0e-463b-b276-8bc283443329" href="https://github.com/mattfelber/CSE-111-programming-with-functions/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span></a>
  
</li>
        <li hidden="" data-menu-item="i5security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-50a11004-4436-4183-a971-f2db1eb3fcbb" href="https://github.com/mattfelber/CSE-111-programming-with-functions/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span></a>
  
</li>
        <li hidden="" data-menu-item="i6insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-5dc70f8e-d908-4eb1-9a5d-ac3085bee324" href="https://github.com/mattfelber/CSE-111-programming-with-functions/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span></a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>
      </div>
</header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full mb-3">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13">Reload</a> to refresh your session.</span>

    <button id="icon-button-6f32dbfa-3200-44a0-8c6a-3aba3c406388" aria-labelledby="tooltip-f364e5f4-e55e-41c8-89df-3abeeb1bbf07" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-f364e5f4-e55e-41c8-89df-3abeeb1bbf07" for="icon-button-6f32dbfa-3200-44a0-8c6a-3aba3c406388" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    
    <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTcyMTAxMjc2IiwidCI6MTcyMDMyMDM0NX0=--d4c5fdbb0bfe52899874f7cac10fcd742acd87950786e05cc6fcdf81ca66ef3c" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst=""></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
  

    






    
  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
    



    
      
<div class="clearfix container-xl px-3 px-md-4 px-lg-5 mt-4">
  <div class="Subhead">
  <h2 class="Subhead-heading">Commit</h2>
</div>

<a href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>




<div id="spoof-warning" class="mt-0 pb-3" hidden="" aria-hidden="">
  <div data-view-component="true" class="flash flash-warn mt-0 clearfix">
  
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert float-left mt-1">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>

      <div class="overflow-hidden">This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.</div>


  
</div></div>


<div class="commit full-commit mt-0 px-2 pt-2 ">
  <div class="d-flex flex-justify-between gap-2">
    <div class="d-flex">
        <span class="mr-1" style="height: 24px">
        </span>

        <div class="commit-title markdown-title">
          chemistry
        </div>
    </div>

    <a id="browse-at-time-link" href="https://github.com/mattfelber/CSE-111-programming-with-functions/tree/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13" class="btn flex-self-start" rel="nofollow" aria-describedby="tooltip-dd3c69b1-b1f2-4a1d-a424-d835a03c2822">Browse files</a>
    <tool-tip id="tooltip-dd3c69b1-b1f2-4a1d-a424-d835a03c2822" for="browse-at-time-link" popover="manual" data-direction="ne" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Browse the repository at this point in the history</tool-tip>
  </div>


  <div class="commit-branches pb-2">
  

    <div class="pt-2">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-branch">
    <path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path>
</svg>
      <ul class="branches-list">
          <li class="branch"><a href="https://github.com/mattfelber/CSE-111-programming-with-functions">main</a></li>
      </ul>
    </div>
</div>


  <div class="commit-meta p-2 d-flex flex-wrap gap-3 flex-column flex-md-row">

    <div class="d-flex flex-1">
      
<div class="AvatarStack flex-self-start  ">
  <div class="AvatarStack-body">
  </div>
</div>

      <div class="flex-self-start flex-content-center">
            <span class="commit-author user-mention" title="mfluxl">mfluxl</span>
    
  committed
  <relative-time datetime="2023-11-26T01:23:15Z" class="no-wrap" title="Nov 26, 2023, 2:23 AM GMT+1"><template shadowrootmode="open">on Nov 26, 2023</template>Nov 26, 2023</relative-time>

        <div class="d-none d-md-inline-block">
          


        </div>
      </div>
    </div>

    <div class="d-flex gap-3 no-wrap text-lg-right text-left overflow-x-auto">
      <span class="sha-block ml-0" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame">
        1 parent
          
          <a class="sha" data-hotkey="p" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/be3a562a027ae02413b4a3d8375278a57e8c3029" data-turbo-frame="repo-content-turbo-frame">be3a562</a>
      </span>
      <span class="sha-block m-0">commit <span class="sha user-select-contain">9515ecf</span></span>
    </div>
  </div>
</div>


  
      <template id="js-inline-comments-single-container-template"></template>



  <diff-layout data-catalyst="">
    <div class="pr-toolbar commit-toolbar mt-n2 color-bg-default d-flex js-sticky-offset-scroll" data-target="diff-layout.diffToolbar">
        <div id="toc" class="d-flex flex-items-center js-details-container Details flex-1 my-2" style="gap: 4px 16px;">
  <file-tree-toggle data-action="toggle-sidebar:diff-layout#toggleSidebar" data-url="/users/emmanuel2011-program/pulls/settings/file_tree_visibility" data-csrf="pMxvC4fD74ol79JQ28UT_cGoJUpN6toM6pBSQUimVM_ikN04dOE9RAaCGKhaumr91FtycDFR6inJEnc-gYhkSA" class="d-none d-md-inline-block d-lg-inline-block d-xl-inline-block" data-catalyst="">
    <div data-view-component="true" class="position-relative d-inline-block">
    <button id="show-file-tree-button" data-target="file-tree-toggle.showFileTreeButton diff-layout.showFileTreeButton" data-action="click:file-tree-toggle#toggleFileTree" data-prefer-file-tree-visible="true" data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;show_tree&quot;,&quot;originating_url&quot;:&quot;https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;,&quot;user_id&quot;:172101276}}" data-hydro-click-hmac="9bd23ec6866bd0dc44ac72039082f22ecee395a9533197628aea300a93400acf" hidden="hidden" type="button" data-view-component="true" class="btn-octicon Link--muted diffbar-item m-0 p-0" aria-labelledby="tooltip-6796a231-f3cc-4949-862f-a6d0e73f6303">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sidebar-collapse">
    <path d="M6.823 7.823a.25.25 0 0 1 0 .354l-2.396 2.396A.25.25 0 0 1 4 10.396V5.604a.25.25 0 0 1 .427-.177Z"></path><path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25H9.5v-13H1.75a.25.25 0 0 0-.25.25ZM11 14.5h3.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11Z"></path>
</svg>
</button>    <tool-tip id="tooltip-6796a231-f3cc-4949-862f-a6d0e73f6303" for="show-file-tree-button" popover="manual" data-direction="ne" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Show file tree</tool-tip>
</div>

    <div data-view-component="true" class="position-relative d-inline-block">
    <button id="hide-file-tree-button" data-target="file-tree-toggle.hideFileTreeButton" data-action="click:file-tree-toggle#toggleFileTree" data-prefer-file-tree-visible="false" data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;hide_tree&quot;,&quot;originating_url&quot;:&quot;https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;,&quot;user_id&quot;:172101276}}" data-hydro-click-hmac="3baac8479c4cb3a2b08835deb2e1236b67f83d4a9fd40f368fd6d1531f64d17a" type="button" data-view-component="true" class="btn-octicon Link--muted diffbar-item m-0 p-0" aria-labelledby="tooltip-3c41324e-b2eb-49db-9560-7c1f1966eab6">      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sidebar-expand">
    <path d="m4.177 7.823 2.396-2.396A.25.25 0 0 1 7 5.604v4.792a.25.25 0 0 1-.427.177L4.177 8.177a.25.25 0 0 1 0-.354Z"></path><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25H9.5v-13Zm12.5 13a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11v13Z"></path>
</svg>
</button>    <tool-tip id="tooltip-3c41324e-b2eb-49db-9560-7c1f1966eab6" for="hide-file-tree-button" popover="manual" data-direction="ne" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Hide file tree</tool-tip>
</div>
</file-tree-toggle>


    <div>
      Showing
      <strong>4 changed files</strong>
      with
      <strong>375 additions</strong>
      and
      <strong>0 deletions</strong>.
    </div>

  <div class="flex-1"></div>
  <div class="d-flex d-inline-block">
    <!-- '"` --><!-- </textarea></xmp> --><form class="d-flex gap-2 flex-column flex-sm-row flex-items-end" data-turbo="false" action="https://github.com/users/diffview" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="TlNDXCEtFw0PXcex_NUWsDmAYPElhc-sluGKsdrnNmeB3nPfxYpgZQU2BNrwBMVcDoRouyWAI6JaQwaIN84zig">
      <segmented-control data-catalyst="">
  <ul aria-label="Whitespace" role="list" data-view-component="true" class="SegmentedControl--small SegmentedControl">
      <li class="SegmentedControl-item SegmentedControl-item--selected" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="w" value="0" data-action="click:segmented-control#select" aria-current="true" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Whitespace">Whitespace</span>
  </span>
</button>

</li>

      <li class="SegmentedControl-item" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="w" value="1" data-action="click:segmented-control#select" aria-current="false" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Ignore whitespace">Ignore whitespace</span>
  </span>
</button>

</li>

</ul></segmented-control>
      <segmented-control data-catalyst="">
  <ul aria-label="Diff view" role="list" data-view-component="true" class="SegmentedControl--small SegmentedControl">
      <li class="SegmentedControl-item" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="diff" value="split" data-action="click:segmented-control#select" aria-current="false" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Split">Split</span>
  </span>
</button>

</li>

      <li class="SegmentedControl-item SegmentedControl-item--selected" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="diff" value="unified" data-action="click:segmented-control#select" aria-current="true" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Unified">Unified</span>
  </span>
</button>

</li>

</ul></segmented-control>
      <input type="hidden" name="old_w" id="old_w" value="0" autocomplete="off" class="form-control">
      <input type="hidden" name="old_diff" id="old_diff" value="unified" autocomplete="off" class="form-control">
</form>  </div>
</div>

    </div>
      <div side="left" responsive="true" data-target="diff-layout.layoutContainer" data-view-component="true" class="Layout Layout--flowRow-until-md Layout--gutter-condensed  hx_Layout wants-full-width-container Layout--sidebarPosition-start Layout--sidebarPosition-flowRow-none">
  
  <div data-target="diff-layout.sidebarContainer" data-action="scroll:diff-layout.sidebarContainer#handleSidebarScroll" data-view-component="true" class="Layout-sidebar overflow-y-auto hx_Layout--sidebar js-notification-shelf-offset-top position-sticky p-2" data-original-top="60px" style="top: 60px !important; height: 867px;">            <div>
              <svg xmlns="http://www.w3.org/2000/svg" hidden="" aria-hidden="true">
  <symbol id="octicon_file-directory-fill_16" viewBox="0 0 16 16" width="16" height="16"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z"></path></symbol><symbol id="octicon_file-submodule_16" viewBox="0 0 16 16" width="16" height="16"><path d="M0 2.75C0 1.784.784 1 1.75 1H5c.55 0 1.07.26 1.4.7l.9 1.2a.25.25 0 0 0 .2.1h6.75c.966 0 1.75.784 1.75 1.75v8.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25Zm9.42 9.36 2.883-2.677a.25.25 0 0 0 0-.366L9.42 6.39a.249.249 0 0 0-.42.183V8.5H4.75a.75.75 0 0 0 0 1.5H9v1.927c0 .218.26.331.42.183Z"></path></symbol><symbol id="octicon_file_16" viewBox="0 0 16 16" width="16" height="16"><path d="M2 1.75C2 .784 2.784 0 3.75 0h6.586c.464 0 .909.184 1.237.513l2.914 2.914c.329.328.513.773.513 1.237v9.586A1.75 1.75 0 0 1 13.25 16h-9.5A1.75 1.75 0 0 1 2 14.25Zm1.75-.25a.25.25 0 0 0-.25.25v12.5c0 .138.112.25.25.25h9.5a.25.25 0 0 0 .25-.25V6h-2.75A1.75 1.75 0 0 1 9 4.25V1.5Zm6.75.062V4.25c0 .138.112.25.25.25h2.688l-.011-.013-2.914-2.914-.013-.011Z"></path></symbol><symbol id="octicon_chevron-down_16" viewBox="0 0 16 16" width="16" height="16"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></symbol><symbol id="octicon_diff-added_16" viewBox="0 0 16 16" width="16" height="16"><path d="M2.75 1h10.5c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 15H2.75A1.75 1.75 0 0 1 1 13.25V2.75C1 1.784 1.784 1 2.75 1Zm10.5 1.5H2.75a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V2.75a.25.25 0 0 0-.25-.25ZM8 4a.75.75 0 0 1 .75.75v2.5h2.5a.75.75 0 0 1 0 1.5h-2.5v2.5a.75.75 0 0 1-1.5 0v-2.5h-2.5a.75.75 0 0 1 0-1.5h2.5v-2.5A.75.75 0 0 1 8 4Z"></path></symbol><symbol id="octicon_diff-removed_16" viewBox="0 0 16 16" width="16" height="16"><path d="M13.25 1c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 15H2.75A1.75 1.75 0 0 1 1 13.25V2.75C1 1.784 1.784 1 2.75 1ZM2.75 2.5a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V2.75a.25.25 0 0 0-.25-.25Zm8.5 6.25h-6.5a.75.75 0 0 1 0-1.5h6.5a.75.75 0 0 1 0 1.5Z"></path></symbol><symbol id="octicon_diff-modified_16" viewBox="0 0 16 16" width="16" height="16"><path d="M13.25 1c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 15H2.75A1.75 1.75 0 0 1 1 13.25V2.75C1 1.784 1.784 1 2.75 1ZM2.75 2.5a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V2.75a.25.25 0 0 0-.25-.25ZM8 10a2 2 0 1 1-.001-3.999A2 2 0 0 1 8 10Z"></path></symbol><symbol id="octicon_diff-renamed_16" viewBox="0 0 16 16" width="16" height="16"><path d="M13.25 1c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 15H2.75A1.75 1.75 0 0 1 1 13.25V2.75C1 1.784 1.784 1 2.75 1ZM2.75 2.5a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V2.75a.25.25 0 0 0-.25-.25Zm9.03 6.03-3.25 3.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l1.97-1.97H4.75a.75.75 0 0 1 0-1.5h4.69L7.47 5.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018l3.25 3.25a.75.75 0 0 1 0 1.06Z"></path></symbol>
</svg>


<div class="subnav-search mx-0 mb-2">
  <input type="text" id="file-tree-filter-field" class="form-control input-block pl-5 js-filterable-field" placeholder="Filter changed files" aria-label="Filter changed files" autocomplete="off" data-target="diff-layout.fileTreePathFilter" data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_filter&quot;,&quot;data&quot;:{&quot;file_count&quot;:4},&quot;pull_request_id&quot;:&quot;9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;,&quot;user_id&quot;:172101276,&quot;action&quot;:&quot;filter_by_pathname&quot;,&quot;originating_url&quot;:&quot;https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;}}" data-hydro-click-hmac="2c9702f38f30dea4348d90e4a9ccdb069d26ba86d353f70b73c0cabd6a9bee47">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search subnav-search-icon">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
</div>
<experimental-action-list data-arrow-navigation="true" data-catalyst="">
  <file-tree data-target="diff-layout.fileTree" data-catalyst="">
    <nav aria-label="File Tree Navigation">
      <ul class="ActionList ActionList--tree ActionList--full" role="tree" aria-label="File Tree" data-filterable-for="file-tree-filter-field" data-filterable-type="substring" data-tree-entry-type="root" data-target="diff-file-filter.treeRoot" data-action="
          filterable:change:diff-file-filter#hideEmptyDirectories
          filterable:change:file-tree#instrumentPathFilterChange
          filterable:change:experimental-action-list#setupFocusZone
        ">
            <li class="ActionList-item ActionList-item--hasSubItem js-tree-node" aria-level="1" role="treeitem" style="--ActionList-tree-depth: 1;" data-skip-substring-filter="" data-tree-entry-type="directory">
    <button class="ActionList-content" aria-expanded="true" type="button" data-action="click:experimental-action-list#handleItemWithSubItemClick" tabindex="0">
      <span class="ActionList-item-action ActionList-item-action--leading">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down ActionList-item-collapseIcon">
    <use href="#octicon_chevron-down_16"></use>
</svg>
      </span>
      <span class="ActionList-item-visual ActionList-item-visual--leading">
        <svg aria-label="Directory" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file-directory-fill hx_color-icon-directory">
    <use href="#octicon_file-directory-fill_16"></use>
</svg>
      </span>
      <span class="ActionList-item-label ActionList-item-label--truncate">
        __pycache__
      </span>
    </button>
    <ul class="ActionList ActionList--subGroup" data-filterable-for="file-tree-filter-field" data-filterable-type="substring" role="group">
          <li id="file-tree-item-diff-08644cc820d91a8c52b0dae9cf0a2e174a2c395a1cd6052ddd530798a5ed6336" class="ActionList-item ActionList-item--subItem js-tree-node" role="treeitem" aria-level="2" style="--ActionList-tree-depth: 2;" data-action="
      click:experimental-action-list#handleItemClick
      click:file-tree#instrumentSelectFile
    " data-target="file-tree.fileTreeNode" data-targets="
      diff-file-filter.treeEntries
      file-tree.fileTreeNodes
    " data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_tree&quot;,&quot;data&quot;:{&quot;file_count&quot;:4,&quot;path&quot;:&quot;__pycache__/chemistry.cpython-311.pyc&quot;,&quot;extension&quot;:&quot;.pyc&quot;},&quot;pull_request_id&quot;:&quot;9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;,&quot;user_id&quot;:172101276,&quot;action&quot;:&quot;file_selected&quot;,&quot;originating_url&quot;:&quot;https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;}}" data-hydro-click-hmac="a267da20aab2b7de825b07b7daff57f7b252950c17d1c533b2d7b7b2cfe60e5f" data-file-type=".pyc" data-file-deleted="false" data-tree-entry-type="file">
    <span data-filterable-item-text="" hidden="">__pycache__/chemistry.cpython-311.pyc</span>
    <a class="ActionList-content hx_ActionList-content" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13#diff-08644cc820d91a8c52b0dae9cf0a2e174a2c395a1cd6052ddd530798a5ed6336" data-turbo="false" tabindex="-1">
      <span class="ActionList-item-visual ActionList-item-visual--leading hx_ActionList-item-visual">
        <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <use href="#octicon_file_16"></use>
</svg>
      </span>
      <span class="ActionList-item-label ActionList-item-label--truncate hx_ActionList-item-label">
        chemistry.cpython-311.pyc
      </span>
      <span class="ActionList-item-visual ActionList-item-visual--trailing hx_ActionList-item-visual">
        <svg title="added" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-diff-added color-fg-success">
    <use href="#octicon_diff-added_16"></use>
</svg>
      </span>
    </a>
  </li>

          <li id="file-tree-item-diff-47bf9e3ea3100ee4bfa2346abd2b2e0b886f85ba660c71f3fd0f19c31c08fa5d" class="ActionList-item ActionList-item--subItem js-tree-node" role="treeitem" aria-level="2" style="--ActionList-tree-depth: 2;" data-action="
      click:experimental-action-list#handleItemClick
      click:file-tree#instrumentSelectFile
    " data-target="file-tree.fileTreeNode" data-targets="
      diff-file-filter.treeEntries
      file-tree.fileTreeNodes
    " data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_tree&quot;,&quot;data&quot;:{&quot;file_count&quot;:4,&quot;path&quot;:&quot;__pycache__/test_chemistry_1.cpython-311-pytest-7.4.3.pyc&quot;,&quot;extension&quot;:&quot;.pyc&quot;},&quot;pull_request_id&quot;:&quot;9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;,&quot;user_id&quot;:172101276,&quot;action&quot;:&quot;file_selected&quot;,&quot;originating_url&quot;:&quot;https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;}}" data-hydro-click-hmac="34db3d1f2ad4867cf9c57fb5013e117e2c4c47ddacf8689936feac4b487185bd" data-file-type=".pyc" data-file-deleted="false" data-tree-entry-type="file">
    <span data-filterable-item-text="" hidden="">__pycache__/test_chemistry_1.cpython-311-pytest-7.4.3.pyc</span>
    <a class="ActionList-content hx_ActionList-content" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13#diff-47bf9e3ea3100ee4bfa2346abd2b2e0b886f85ba660c71f3fd0f19c31c08fa5d" data-turbo="false" tabindex="-1">
      <span class="ActionList-item-visual ActionList-item-visual--leading hx_ActionList-item-visual">
        <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <use href="#octicon_file_16"></use>
</svg>
      </span>
      <span class="ActionList-item-label ActionList-item-label--truncate hx_ActionList-item-label">
        test_chemistry_1.cpython-311-pytest-7.4.3.pyc
      </span>
      <span class="ActionList-item-visual ActionList-item-visual--trailing hx_ActionList-item-visual">
        <svg title="added" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-diff-added color-fg-success">
    <use href="#octicon_diff-added_16"></use>
</svg>
      </span>
    </a>
  </li>

    </ul>
  </li>

            <li id="file-tree-item-diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" class="ActionList-item js-tree-node" role="treeitem" aria-level="1" style="--ActionList-tree-depth: 1;" data-action="
      click:experimental-action-list#handleItemClick
      click:file-tree#instrumentSelectFile
    " data-target="file-tree.fileTreeNode" data-targets="
      diff-file-filter.treeEntries
      file-tree.fileTreeNodes
    " data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_tree&quot;,&quot;data&quot;:{&quot;file_count&quot;:4,&quot;path&quot;:&quot;chemistry.py&quot;,&quot;extension&quot;:&quot;.py&quot;},&quot;pull_request_id&quot;:&quot;9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;,&quot;user_id&quot;:172101276,&quot;action&quot;:&quot;file_selected&quot;,&quot;originating_url&quot;:&quot;https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;}}" data-hydro-click-hmac="47694244c7f85425e678ed01e5969e555caed818034284465753e428e0a0263c" data-file-type=".py" data-file-deleted="false" data-tree-entry-type="file">
    <span data-filterable-item-text="" hidden="">chemistry.py</span>
    <a class="ActionList-content hx_ActionList-content" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13#diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-turbo="false" tabindex="-1">
      <span class="ActionList-item-visual ActionList-item-visual--leading hx_ActionList-item-visual">
        <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <use href="#octicon_file_16"></use>
</svg>
      </span>
      <span class="ActionList-item-label ActionList-item-label--truncate hx_ActionList-item-label">
        chemistry.py
      </span>
      <span class="ActionList-item-visual ActionList-item-visual--trailing hx_ActionList-item-visual">
        <svg title="added" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-diff-added color-fg-success">
    <use href="#octicon_diff-added_16"></use>
</svg>
      </span>
    </a>
  </li>

            <li id="file-tree-item-diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" class="ActionList-item js-tree-node" role="treeitem" aria-level="1" style="--ActionList-tree-depth: 1;" data-action="
      click:experimental-action-list#handleItemClick
      click:file-tree#instrumentSelectFile
    " data-target="file-tree.fileTreeNode" data-targets="
      diff-file-filter.treeEntries
      file-tree.fileTreeNodes
    " data-hydro-click-payload="{&quot;event_type&quot;:&quot;pull_request.user_action&quot;,&quot;payload&quot;:{&quot;category&quot;:&quot;file_tree&quot;,&quot;data&quot;:{&quot;file_count&quot;:4,&quot;path&quot;:&quot;test_chemistry_1.py&quot;,&quot;extension&quot;:&quot;.py&quot;},&quot;pull_request_id&quot;:&quot;9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;,&quot;user_id&quot;:172101276,&quot;action&quot;:&quot;file_selected&quot;,&quot;originating_url&quot;:&quot;https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;}}" data-hydro-click-hmac="ce10bcf2d9a6e735ee8d741a48bf5b95f9db69a5dc3fddcc7615f87d94bd0ccf" data-file-type=".py" data-file-deleted="false" data-tree-entry-type="file">
    <span data-filterable-item-text="" hidden="">test_chemistry_1.py</span>
    <a class="ActionList-content hx_ActionList-content" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13#diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-turbo="false" tabindex="-1">
      <span class="ActionList-item-visual ActionList-item-visual--leading hx_ActionList-item-visual">
        <svg aria-label="File" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-file color-fg-muted">
    <use href="#octicon_file_16"></use>
</svg>
      </span>
      <span class="ActionList-item-label ActionList-item-label--truncate hx_ActionList-item-label">
        test_chemistry_1.py
      </span>
      <span class="ActionList-item-visual ActionList-item-visual--trailing hx_ActionList-item-visual">
        <svg title="added" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-diff-added color-fg-success">
    <use href="#octicon_diff-added_16"></use>
</svg>
      </span>
    </a>
  </li>

      </ul>
    </nav>
  </file-tree>
</experimental-action-list>

            </div>
</div>
  <div data-target="diff-layout.mainContainer" data-view-component="true" class="Layout-main files-next-bucket">          <a name="diff-stat"></a>
          
<template class="js-comment-button-template"></template>

<div id="files" class="diff-view commentable js-diff-container js-code-nav-container" data-hpc="">


  <div class="container-md js-file-filter-blankslate" data-target="diff-file-filter.blankslate" hidden="">
    
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-filter blankslate-icon">
    <path d="M2.75 6a.75.75 0 0 0 0 1.5h18.5a.75.75 0 0 0 0-1.5H2.75ZM6 11.75a.75.75 0 0 1 .75-.75h10.5a.75.75 0 0 1 0 1.5H6.75a.75.75 0 0 1-.75-.75Zm4 4.938a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>

      <h2 data-view-component="true" class="blankslate-heading">        There are no files selected for viewing
</h2>
      

</div>  </div>
  </div>
  <div class="js-diff-progressive-container">
    <copilot-diff-entry data-file-path="__pycache__/chemistry.cpython-311.pyc" data-disabled="">
  <div id="diff-08644cc820d91a8c52b0dae9cf0a2e174a2c395a1cd6052ddd530798a5ed6336" data-details-container-group="file" class="file js-file js-details-container js-targetable-element show-inline-notes Details
               Details--on open
              
              
              
              
              
              js-tagsearch-file" data-file-type=".pyc" data-file-deleted="false" data-tagsearch-path="__pycache__/chemistry.cpython-311.pyc" data-tagsearch-lang="" data-targets="diff-file-filter.diffEntries">
    <div class="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch " data-path="__pycache__/chemistry.cpython-311.pyc" data-short-path="08644cc" data-anchor="diff-08644cc820d91a8c52b0dae9cf0a2e174a2c395a1cd6052ddd530798a5ed6336" data-file-type=".pyc" data-file-deleted="false">
      <div class="file-info flex-auto min-width-0 mb-md-0 mb-2">
        <button type="button" class="btn-octicon js-details-target" aria-label="Toggle diff contents" aria-expanded="true" style="width: 22px;">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down Details-content--hidden">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right Details-content--shown">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>




          <span class="sr-only">Binary file added</span>
          <span class="diffstat" aria-hidden="true">
            BIN
              <span class="color-fg-success">
                +5.8 KB

              </span>
          </span>

        
<span class="Truncate">
  <a title="__pycache__/chemistry.cpython-311.pyc" class="Link--primary Truncate-text" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13#diff-08644cc820d91a8c52b0dae9cf0a2e174a2c395a1cd6052ddd530798a5ed6336">__pycache__/chemistry.cpython-311.pyc</a>

  <span data-view-component="true">
  <clipboard-copy data-copy-feedback="Copied!" aria-label="Copy" value="__pycache__/chemistry.cpython-311.pyc" data-view-component="true" class="Link--onHover color-fg-muted ml-2 mr-2" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg style="display: none;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</clipboard-copy>  <div aria-live="polite" aria-atomic="true" class="sr-only" data-clipboard-copy-feedback=""></div>
</span>
</span>


        
      </div>

      <div class="file-actions pt-0 mb-md-0 mb-2 ml-md-2 flex-shrink-0 flex-md-justify-end">
        <div class="d-flex flex-justify-end">











          

          <details class="js-file-header-dropdown dropdown details-overlay details-reset pr-2 pl-2">
            <summary class="height-full" aria-haspopup="menu" role="button">
              <div class="height-full d-flex flex-items-center Link--secondary">
                <svg aria-label="Show options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
              </div>
            </summary>
            <details-menu class="dropdown-menu dropdown-menu-sw show-more-popover color-fg-default position-absolute f5" style="width:fit-content; min-width:185px; z-index:99; right: -4px;" role="menu" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
                            <label role="menuitemradio" class="dropdown-item btn-link text-normal d-block pl-5" tabindex="0" aria-checked="true">
              <span class="position-absolute ml-n4"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg></span>
              <input type="checkbox" checked="" class="d-none js-toggle-file-notes">
              Show comments
            </label>

                            <div role="none" class="dropdown-divider"></div>

                              <a href="https://github.com/mattfelber/CSE-111-programming-with-functions/blob/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13/__pycache__/chemistry.cpython-311.pyc" class="pl-5 dropdown-item btn-link" rel="nofollow" role="menuitem" data-ga-click="View file, click, location:files_changed_dropdown">
   View file
</a>


                                    <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to make changes.">
      Edit file
    </button>


                                  <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to delete this file.">
    Delete file
  </button>


                            <div role="none" class="dropdown-divider"></div>

                            <span data-target="copilot-diff-entry.menuItemsSlot"></span>

                
            <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
          </details>
        </div>
      </div>
    </div>


    <div class="js-file-content Details-content--hidden position-relative" data-hydro-view="{&quot;event_type&quot;:&quot;pull_request.select_diff_range&quot;,&quot;payload&quot;:{&quot;actor_id&quot;:172101276,&quot;pull_request_id&quot;:null,&quot;repository_id&quot;:null,&quot;diff_type&quot;:&quot;UNIFIED&quot;,&quot;whitespace_ignored&quot;:false,&quot;originating_url&quot;:&quot;https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;,&quot;user_id&quot;:172101276}}" data-hydro-view-hmac="2f7f8694ae5e0febe5d7308a3362e20c14b5dbb6b7f3b8f9cb0e38f3cd5e650e">
          <div class="data highlight empty">
            Binary file not shown.
          </div>

    </div>
  </div>
</copilot-diff-entry>

    <copilot-diff-entry data-file-path="__pycache__/test_chemistry_1.cpython-311-pytest-7.4.3.pyc" data-disabled="">
  <div id="diff-47bf9e3ea3100ee4bfa2346abd2b2e0b886f85ba660c71f3fd0f19c31c08fa5d" data-details-container-group="file" class="file js-file js-details-container js-targetable-element show-inline-notes Details
               Details--on open
              
              
              
              
              
              js-tagsearch-file" data-file-type=".pyc" data-file-deleted="false" data-tagsearch-path="__pycache__/test_chemistry_1.cpython-311-pytest-7.4.3.pyc" data-tagsearch-lang="" data-targets="diff-file-filter.diffEntries">
    <div class="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch " data-path="__pycache__/test_chemistry_1.cpython-311-pytest-7.4.3.pyc" data-short-path="47bf9e3" data-anchor="diff-47bf9e3ea3100ee4bfa2346abd2b2e0b886f85ba660c71f3fd0f19c31c08fa5d" data-file-type=".pyc" data-file-deleted="false">
      <div class="file-info flex-auto min-width-0 mb-md-0 mb-2">
        <button type="button" class="btn-octicon js-details-target" aria-label="Toggle diff contents" aria-expanded="true" style="width: 22px;">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down Details-content--hidden">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right Details-content--shown">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>




          <span class="sr-only">Binary file added</span>
          <span class="diffstat" aria-hidden="true">
            BIN
              <span class="color-fg-success">
                +17.8 KB

              </span>
          </span>

        
<span class="Truncate">
  <a title="__pycache__/test_chemistry_1.cpython-311-pytest-7.4.3.pyc" class="Link--primary Truncate-text" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13#diff-47bf9e3ea3100ee4bfa2346abd2b2e0b886f85ba660c71f3fd0f19c31c08fa5d">__pycache__/test_chemistry_1.cpython-311-pytest-7.4.3.pyc</a>

  <span data-view-component="true">
  <clipboard-copy data-copy-feedback="Copied!" aria-label="Copy" value="__pycache__/test_chemistry_1.cpython-311-pytest-7.4.3.pyc" data-view-component="true" class="Link--onHover color-fg-muted ml-2 mr-2" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg style="display: none;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</clipboard-copy>  <div aria-live="polite" aria-atomic="true" class="sr-only" data-clipboard-copy-feedback=""></div>
</span>
</span>


        
      </div>

      <div class="file-actions pt-0 mb-md-0 mb-2 ml-md-2 flex-shrink-0 flex-md-justify-end">
        <div class="d-flex flex-justify-end">











          

          <details class="js-file-header-dropdown dropdown details-overlay details-reset pr-2 pl-2">
            <summary class="height-full" aria-haspopup="menu" role="button">
              <div class="height-full d-flex flex-items-center Link--secondary">
                <svg aria-label="Show options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
              </div>
            </summary>
            <details-menu class="dropdown-menu dropdown-menu-sw show-more-popover color-fg-default position-absolute f5" style="width:fit-content; min-width:185px; z-index:99; right: -4px;" role="menu" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
                            <label role="menuitemradio" class="dropdown-item btn-link text-normal d-block pl-5" tabindex="0" aria-checked="true">
              <span class="position-absolute ml-n4"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg></span>
              <input type="checkbox" checked="" class="d-none js-toggle-file-notes">
              Show comments
            </label>

                            <div role="none" class="dropdown-divider"></div>

                              <a href="https://github.com/mattfelber/CSE-111-programming-with-functions/blob/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13/__pycache__/test_chemistry_1.cpython-311-pytest-7.4.3.pyc" class="pl-5 dropdown-item btn-link" rel="nofollow" role="menuitem" data-ga-click="View file, click, location:files_changed_dropdown">
   View file
</a>


                                    <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to make changes.">
      Edit file
    </button>


                                  <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to delete this file.">
    Delete file
  </button>


                            <div role="none" class="dropdown-divider"></div>

                            <span data-target="copilot-diff-entry.menuItemsSlot"></span>

                
            <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
          </details>
        </div>
      </div>
    </div>


    <div class="js-file-content Details-content--hidden position-relative" data-hydro-view="{&quot;event_type&quot;:&quot;pull_request.select_diff_range&quot;,&quot;payload&quot;:{&quot;actor_id&quot;:172101276,&quot;pull_request_id&quot;:null,&quot;repository_id&quot;:null,&quot;diff_type&quot;:&quot;UNIFIED&quot;,&quot;whitespace_ignored&quot;:false,&quot;originating_url&quot;:&quot;https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;,&quot;user_id&quot;:172101276}}" data-hydro-view-hmac="2f7f8694ae5e0febe5d7308a3362e20c14b5dbb6b7f3b8f9cb0e38f3cd5e650e">
          <div class="data highlight empty">
            Binary file not shown.
          </div>

    </div>
  </div>
</copilot-diff-entry>

    <copilot-diff-entry data-file-path="chemistry.py">
  <div id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-details-container-group="file" class="file js-file js-details-container js-targetable-element show-inline-notes Details
               Details--on open
              
              
              
              
              
              js-tagsearch-file" data-file-type=".py" data-file-deleted="false" data-tagsearch-path="chemistry.py" data-tagsearch-lang="Python" data-targets="diff-file-filter.diffEntries">
    <div class="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch " data-path="chemistry.py" data-short-path="72c1c0f" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-file-type=".py" data-file-deleted="false">
      <div class="file-info flex-auto min-width-0 mb-md-0 mb-2">
        <button type="button" class="btn-octicon js-details-target" aria-label="Toggle diff contents" aria-expanded="true" style="width: 22px;">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down Details-content--hidden">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right Details-content--shown">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>




          <span class="sr-only">
            120 changes: 120 additions &amp; 0 deletions
          </span>
          <span class="diffstat" aria-hidden="true">120 <span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span></span>

        
<span class="Truncate">
  <a title="chemistry.py" class="Link--primary Truncate-text" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13#diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289">chemistry.py</a>

  <span data-view-component="true">
  <clipboard-copy data-copy-feedback="Copied!" aria-label="Copy" value="chemistry.py" data-view-component="true" class="Link--onHover color-fg-muted ml-2 mr-2" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg style="display: none;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</clipboard-copy>  <div aria-live="polite" aria-atomic="true" class="sr-only" data-clipboard-copy-feedback=""></div>
</span>
</span>


        
      </div>

      <div class="file-actions pt-0 mb-md-0 mb-2 ml-md-2 flex-shrink-0 flex-md-justify-end">
        <div class="d-flex flex-justify-end">











          

          <details class="js-file-header-dropdown dropdown details-overlay details-reset pr-2 pl-2">
            <summary class="height-full" aria-haspopup="menu" role="button">
              <div class="height-full d-flex flex-items-center Link--secondary">
                <svg aria-label="Show options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
              </div>
            </summary>
            <details-menu class="dropdown-menu dropdown-menu-sw show-more-popover color-fg-default position-absolute f5" style="width:fit-content; min-width:185px; z-index:99; right: -4px;" role="menu" data-focus-trap="suspended"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
                            <label role="menuitemradio" class="dropdown-item btn-link text-normal d-block pl-5" tabindex="0" aria-checked="true">
              <span class="position-absolute ml-n4"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg></span>
              <input type="checkbox" checked="" class="d-none js-toggle-file-notes">
              Show comments
            </label>

                            <div role="none" class="dropdown-divider"></div>

                              <a href="https://github.com/mattfelber/CSE-111-programming-with-functions/blob/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13/chemistry.py" class="pl-5 dropdown-item btn-link" rel="nofollow" role="menuitem" data-ga-click="View file, click, location:files_changed_dropdown">
   View file
</a>


                                    <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to make changes.">
      Edit file
    </button>


                                  <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to delete this file.">
    Delete file
  </button>


                            <div role="none" class="dropdown-divider"></div>

                            <span data-target="copilot-diff-entry.menuItemsSlot"></span>

                
            <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
          </details>
        </div>
      </div>
    </div>


    <div class="js-file-content Details-content--hidden position-relative" data-hydro-view="{&quot;event_type&quot;:&quot;pull_request.select_diff_range&quot;,&quot;payload&quot;:{&quot;actor_id&quot;:172101276,&quot;pull_request_id&quot;:null,&quot;repository_id&quot;:null,&quot;diff_type&quot;:&quot;UNIFIED&quot;,&quot;whitespace_ignored&quot;:false,&quot;originating_url&quot;:&quot;https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;,&quot;user_id&quot;:172101276}}" data-hydro-view-hmac="2f7f8694ae5e0febe5d7308a3362e20c14b5dbb6b7f3b8f9cb0e38f3cd5e650e" data-hydro-client-context="{&quot;starting_diff_position&quot;:&quot;R1&quot;,&quot;ending_diff_position&quot;:&quot;R102&quot;,&quot;line_count&quot;:102}">


          <div class="data highlight js-blob-wrapper">
            <template class="js-file-alert-template"></template>
<template class="js-line-alert-template"></template>



              
              <table class="diff-table js-diff-table tab-size" data-tab-size="8" data-diff-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-paste-markdown-skip="">
                <thead class="sr-only">
                  <tr>
                      <th scope="col">Original file line number</th>
                      <th scope="col">Diff line number</th>
                      <th scope="col">Diff line change</th>
                  </tr>
                </thead>
                <tbody>
                      
      <tr data-position="0">
    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289HL0" class="blob-num blob-num-hunk non-expandable" data-line-number="..."></td>
    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289HR1" class="blob-num blob-num-hunk non-expandable" data-line-number="..."></td>
    <td class="blob-code blob-code-inner blob-code-hunk">@@ -0,0 +1,120 @@</td>
  </tr>

    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R1" data-line-number="1" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="1" data-side="right" data-line="1" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R2" data-line-number="2" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="2" data-side="right" data-line="2" data-original-line="+def main():" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">main</span>():</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R3" data-line-number="3" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="3" data-side="right" data-line="3" data-original-line="+    print(&quot;Welcome to the Mole Calculator. After entering the Chemical Formula, enter the Mass of the sample in Grams.&quot;)" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">print</span>(<span class="pl-s">"Welcome to the Mole Calculator. After entering the Chemical Formula, enter the Mass of the sample in Grams."</span>)</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R4" data-line-number="4" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="4" data-side="right" data-line="4" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R5" data-line-number="5" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="5" data-side="right" data-line="5" data-original-line="+    formula = str(input(&quot;Enter the Formula of you Chemical Compound: &quot;))" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">formula</span> <span class="pl-c1">=</span> <span class="pl-en">str</span>(<span class="pl-en">input</span>(<span class="pl-s">"Enter the Formula of you Chemical Compound: "</span>))</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R6" data-line-number="6" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="6" data-side="right" data-line="6" data-original-line="+    weight = float(input(&quot;Enter the Mass of the Sample in Grams: &quot;))" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">weight</span> <span class="pl-c1">=</span> <span class="pl-en">float</span>(<span class="pl-en">input</span>(<span class="pl-s">"Enter the Mass of the Sample in Grams: "</span>))</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R7" data-line-number="7" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="7" data-side="right" data-line="7" data-original-line="+    periodic_table_list = make_periodic_table(formula, weight)" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">periodic_table_list</span> <span class="pl-c1">=</span> <span class="pl-en">make_periodic_table</span>(<span class="pl-s1">formula</span>, <span class="pl-s1">weight</span>)</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R8" data-line-number="8" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="8" data-side="right" data-line="8" data-original-line="+    " aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R9" data-line-number="9" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="9" data-side="right" data-line="9" data-original-line="+    for item in periodic_table_list:" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">for</span> <span class="pl-s1">item</span> <span class="pl-c1">in</span> <span class="pl-s1">periodic_table_list</span>:</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R10" data-line-number="10" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="10" data-side="right" data-line="10" data-original-line="+        print(f&quot;{item[1]} {item[2]}&quot;)" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-en">print</span>(<span class="pl-s">f"<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">item</span>[<span class="pl-c1">1</span>]<span class="pl-kos">}</span></span> <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">item</span>[<span class="pl-c1">2</span>]<span class="pl-kos">}</span></span>"</span>)</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R11" data-line-number="11" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="11" data-side="right" data-line="11" data-original-line="+    " aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R12" data-line-number="12" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="12" data-side="right" data-line="12" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R13" data-line-number="13" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="13" data-side="right" data-line="13" data-original-line="+def make_periodic_table(formula, weight):" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">make_periodic_table</span>(<span class="pl-s1">formula</span>, <span class="pl-s1">weight</span>):</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R14" data-line-number="14" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="14" data-side="right" data-line="14" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R15" data-line-number="15" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="15" data-side="right" data-line="15" data-original-line="+    periodic_table_list = [" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">periodic_table_list</span> <span class="pl-c1">=</span> [</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R16" data-line-number="16" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="16" data-side="right" data-line="16" data-original-line="+    # [symbol, name, atomic_mass]]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c"># [symbol, name, atomic_mass]],</span></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R17" data-line-number="17" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="17" data-side="right" data-line="17" data-original-line="+    [&quot;Ac&quot;,	&quot;Actinium&quot;,	227]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ac"</span>,	<span class="pl-s">"Actinium"</span>,	<span class="pl-c1">227</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R18" data-line-number="18" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="18" data-side="right" data-line="18" data-original-line="+    [&quot;Ag&quot;,	&quot;Silver&quot;,	107.8682]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ag"</span>,	<span class="pl-s">"Silver"</span>,	<span class="pl-c1">107.8682</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R19" data-line-number="19" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="19" data-side="right" data-line="19" data-original-line="+    [&quot;Al&quot;,	&quot;Aluminum&quot;,	26.9815386]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Al"</span>,	<span class="pl-s">"Aluminum"</span>,	<span class="pl-c1">26.9815386</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R20" data-line-number="20" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="20" data-side="right" data-line="20" data-original-line="+    [&quot;Ar&quot;,	&quot;Argon&quot;,	39.948]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ar"</span>,	<span class="pl-s">"Argon"</span>,	<span class="pl-c1">39.948</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R21" data-line-number="21" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="21" data-side="right" data-line="21" data-original-line="+    [&quot;As&quot;,	&quot;Arsenic&quot;,	74.9216]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"As"</span>,	<span class="pl-s">"Arsenic"</span>,	<span class="pl-c1">74.9216</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R22" data-line-number="22" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="22" data-side="right" data-line="22" data-original-line="+    [&quot;At&quot;,	&quot;Astatine&quot;,	210]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"At"</span>,	<span class="pl-s">"Astatine"</span>,	<span class="pl-c1">210</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R23" data-line-number="23" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="23" data-side="right" data-line="23" data-original-line="+    [&quot;Au&quot;,	&quot;Gold&quot;,	196.966569]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Au"</span>,	<span class="pl-s">"Gold"</span>,	<span class="pl-c1">196.966569</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R24" data-line-number="24" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="24" data-side="right" data-line="24" data-original-line="+    [&quot;B&quot;,	&quot;Boron&quot;,	10.811]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"B"</span>,	<span class="pl-s">"Boron"</span>,	<span class="pl-c1">10.811</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R25" data-line-number="25" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="25" data-side="right" data-line="25" data-original-line="+    [&quot;Ba&quot;,	&quot;Barium&quot;,	137.327]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ba"</span>,	<span class="pl-s">"Barium"</span>,	<span class="pl-c1">137.327</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R26" data-line-number="26" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="26" data-side="right" data-line="26" data-original-line="+    [&quot;Be&quot;,	&quot;Beryllium&quot;,	9.012182]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Be"</span>,	<span class="pl-s">"Beryllium"</span>,	<span class="pl-c1">9.012182</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R27" data-line-number="27" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="27" data-side="right" data-line="27" data-original-line="+    [&quot;Bi&quot;,	&quot;Bismuth&quot;,	208.9804]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Bi"</span>,	<span class="pl-s">"Bismuth"</span>,	<span class="pl-c1">208.9804</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R28" data-line-number="28" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="28" data-side="right" data-line="28" data-original-line="+    [&quot;Br&quot;,	&quot;Bromine&quot;,	79.904]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Br"</span>,	<span class="pl-s">"Bromine"</span>,	<span class="pl-c1">79.904</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R29" data-line-number="29" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="29" data-side="right" data-line="29" data-original-line="+    [&quot;C&quot;,	&quot;Carbon&quot;,	12.0107]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"C"</span>,	<span class="pl-s">"Carbon"</span>,	<span class="pl-c1">12.0107</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R30" data-line-number="30" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="30" data-side="right" data-line="30" data-original-line="+    [&quot;Ca&quot;,	&quot;Calcium&quot;,	40.078]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ca"</span>,	<span class="pl-s">"Calcium"</span>,	<span class="pl-c1">40.078</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R31" data-line-number="31" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="31" data-side="right" data-line="31" data-original-line="+    [&quot;Cd&quot;,	&quot;Cadmium&quot;,	112.411]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Cd"</span>,	<span class="pl-s">"Cadmium"</span>,	<span class="pl-c1">112.411</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R32" data-line-number="32" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="32" data-side="right" data-line="32" data-original-line="+    [&quot;Ce&quot;,	&quot;Cerium&quot;,	140.116]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ce"</span>,	<span class="pl-s">"Cerium"</span>,	<span class="pl-c1">140.116</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R33" data-line-number="33" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="33" data-side="right" data-line="33" data-original-line="+    [&quot;Cl&quot;,	&quot;Chlorine&quot;,	35.453]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Cl"</span>,	<span class="pl-s">"Chlorine"</span>,	<span class="pl-c1">35.453</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R34" data-line-number="34" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="34" data-side="right" data-line="34" data-original-line="+    [&quot;Co&quot;,	&quot;Cobalt&quot;,	58.933195]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Co"</span>,	<span class="pl-s">"Cobalt"</span>,	<span class="pl-c1">58.933195</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R35" data-line-number="35" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="35" data-side="right" data-line="35" data-original-line="+    [&quot;Cr&quot;,	&quot;Chromium&quot;,	51.9961]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Cr"</span>,	<span class="pl-s">"Chromium"</span>,	<span class="pl-c1">51.9961</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R36" data-line-number="36" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="36" data-side="right" data-line="36" data-original-line="+    [&quot;Cs&quot;,	&quot;Cesium&quot;,	132.9054519]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Cs"</span>,	<span class="pl-s">"Cesium"</span>,	<span class="pl-c1">132.9054519</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R37" data-line-number="37" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="37" data-side="right" data-line="37" data-original-line="+    [&quot;Cu&quot;,	&quot;Copper&quot;,	63.546]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Cu"</span>,	<span class="pl-s">"Copper"</span>,	<span class="pl-c1">63.546</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R38" data-line-number="38" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="38" data-side="right" data-line="38" data-original-line="+    [&quot;Dy&quot;,	&quot;Dysprosium&quot;,	162.5]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Dy"</span>,	<span class="pl-s">"Dysprosium"</span>,	<span class="pl-c1">162.5</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R39" data-line-number="39" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="39" data-side="right" data-line="39" data-original-line="+    [&quot;Er&quot;,	&quot;Erbium&quot;,	167.259]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Er"</span>,	<span class="pl-s">"Erbium"</span>,	<span class="pl-c1">167.259</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R40" data-line-number="40" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="40" data-side="right" data-line="40" data-original-line="+    [&quot;Eu&quot;,	&quot;Europium&quot;,	151.964]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Eu"</span>,	<span class="pl-s">"Europium"</span>,	<span class="pl-c1">151.964</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R41" data-line-number="41" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="41" data-side="right" data-line="41" data-original-line="+    [&quot;F&quot;,	&quot;Fluorine&quot;,	18.9984032]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"F"</span>,	<span class="pl-s">"Fluorine"</span>,	<span class="pl-c1">18.9984032</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R42" data-line-number="42" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="42" data-side="right" data-line="42" data-original-line="+    [&quot;Fe&quot;,	&quot;Iron&quot;,	55.845]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Fe"</span>,	<span class="pl-s">"Iron"</span>,	<span class="pl-c1">55.845</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R43" data-line-number="43" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="43" data-side="right" data-line="43" data-original-line="+    [&quot;Fr&quot;,	&quot;Francium&quot;,	223]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Fr"</span>,	<span class="pl-s">"Francium"</span>,	<span class="pl-c1">223</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R44" data-line-number="44" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="44" data-side="right" data-line="44" data-original-line="+    [&quot;Ga&quot;,	&quot;Gallium&quot;,	69.723]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ga"</span>,	<span class="pl-s">"Gallium"</span>,	<span class="pl-c1">69.723</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R45" data-line-number="45" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="45" data-side="right" data-line="45" data-original-line="+    [&quot;Gd&quot;,	&quot;Gadolinium&quot;,	157.25]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Gd"</span>,	<span class="pl-s">"Gadolinium"</span>,	<span class="pl-c1">157.25</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R46" data-line-number="46" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="46" data-side="right" data-line="46" data-original-line="+    [&quot;Ge&quot;,	&quot;Germanium&quot;,	72.64]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ge"</span>,	<span class="pl-s">"Germanium"</span>,	<span class="pl-c1">72.64</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R47" data-line-number="47" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="47" data-side="right" data-line="47" data-original-line="+    [&quot;H&quot;,	&quot;Hydrogen&quot;,	1.00794]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"H"</span>,	<span class="pl-s">"Hydrogen"</span>,	<span class="pl-c1">1.00794</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R48" data-line-number="48" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="48" data-side="right" data-line="48" data-original-line="+    [&quot;He&quot;,	&quot;Helium&quot;,	4.002602]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"He"</span>,	<span class="pl-s">"Helium"</span>,	<span class="pl-c1">4.002602</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R49" data-line-number="49" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="49" data-side="right" data-line="49" data-original-line="+    [&quot;Hf&quot;,	&quot;Hafnium&quot;,	178.49]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Hf"</span>,	<span class="pl-s">"Hafnium"</span>,	<span class="pl-c1">178.49</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R50" data-line-number="50" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="50" data-side="right" data-line="50" data-original-line="+    [&quot;Hg&quot;,	&quot;Mercury&quot;,	200.59]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Hg"</span>,	<span class="pl-s">"Mercury"</span>,	<span class="pl-c1">200.59</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R51" data-line-number="51" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="51" data-side="right" data-line="51" data-original-line="+    [&quot;Ho&quot;,	&quot;Holmium&quot;,	164.93032]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ho"</span>,	<span class="pl-s">"Holmium"</span>,	<span class="pl-c1">164.93032</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R52" data-line-number="52" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="52" data-side="right" data-line="52" data-original-line="+    [&quot;I&quot;,	&quot;Iodine&quot;,	126.90447]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"I"</span>,	<span class="pl-s">"Iodine"</span>,	<span class="pl-c1">126.90447</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R53" data-line-number="53" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="53" data-side="right" data-line="53" data-original-line="+    [&quot;In&quot;,	&quot;Indium&quot;,	114.818]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"In"</span>,	<span class="pl-s">"Indium"</span>,	<span class="pl-c1">114.818</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R54" data-line-number="54" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="54" data-side="right" data-line="54" data-original-line="+    [&quot;Ir&quot;,	&quot;Iridium&quot;,	192.217]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ir"</span>,	<span class="pl-s">"Iridium"</span>,	<span class="pl-c1">192.217</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R55" data-line-number="55" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="55" data-side="right" data-line="55" data-original-line="+    [&quot;K&quot;,	&quot;Potassium&quot;,	39.0983]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"K"</span>,	<span class="pl-s">"Potassium"</span>,	<span class="pl-c1">39.0983</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R56" data-line-number="56" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="56" data-side="right" data-line="56" data-original-line="+    [&quot;Kr&quot;,	&quot;Krypton&quot;,	83.798]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Kr"</span>,	<span class="pl-s">"Krypton"</span>,	<span class="pl-c1">83.798</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R57" data-line-number="57" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="57" data-side="right" data-line="57" data-original-line="+    [&quot;La&quot;,	&quot;Lanthanum&quot;,	138.90547]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"La"</span>,	<span class="pl-s">"Lanthanum"</span>,	<span class="pl-c1">138.90547</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R58" data-line-number="58" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="58" data-side="right" data-line="58" data-original-line="+    [&quot;Li&quot;,	&quot;Lithium&quot;,	6.941]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Li"</span>,	<span class="pl-s">"Lithium"</span>,	<span class="pl-c1">6.941</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R59" data-line-number="59" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="59" data-side="right" data-line="59" data-original-line="+    [&quot;Lu&quot;,	&quot;Lutetium&quot;,	174.9668]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Lu"</span>,	<span class="pl-s">"Lutetium"</span>,	<span class="pl-c1">174.9668</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R60" data-line-number="60" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="60" data-side="right" data-line="60" data-original-line="+    [&quot;Mg&quot;,	&quot;Magnesium&quot;,	24.305]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Mg"</span>,	<span class="pl-s">"Magnesium"</span>,	<span class="pl-c1">24.305</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R61" data-line-number="61" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="61" data-side="right" data-line="61" data-original-line="+    [&quot;Mn&quot;,	&quot;Manganese&quot;,	54.938045]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Mn"</span>,	<span class="pl-s">"Manganese"</span>,	<span class="pl-c1">54.938045</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R62" data-line-number="62" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="62" data-side="right" data-line="62" data-original-line="+    [&quot;Mo&quot;,	&quot;Molybdenum&quot;,	95.96]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Mo"</span>,	<span class="pl-s">"Molybdenum"</span>,	<span class="pl-c1">95.96</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R63" data-line-number="63" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="63" data-side="right" data-line="63" data-original-line="+    [&quot;N&quot;,	&quot;Nitrogen&quot;,	14.0067]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"N"</span>,	<span class="pl-s">"Nitrogen"</span>,	<span class="pl-c1">14.0067</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R64" data-line-number="64" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="64" data-side="right" data-line="64" data-original-line="+    [&quot;Na&quot;,	&quot;Sodium&quot;,	22.98976928]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Na"</span>,	<span class="pl-s">"Sodium"</span>,	<span class="pl-c1">22.98976928</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R65" data-line-number="65" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="65" data-side="right" data-line="65" data-original-line="+    [&quot;Nb&quot;,	&quot;Niobium&quot;,	92.90638]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Nb"</span>,	<span class="pl-s">"Niobium"</span>,	<span class="pl-c1">92.90638</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R66" data-line-number="66" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="66" data-side="right" data-line="66" data-original-line="+    [&quot;Nd&quot;,	&quot;Neodymium&quot;,	144.242]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Nd"</span>,	<span class="pl-s">"Neodymium"</span>,	<span class="pl-c1">144.242</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R67" data-line-number="67" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="67" data-side="right" data-line="67" data-original-line="+    [&quot;Ne&quot;,	&quot;Neon&quot;,	20.1797]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ne"</span>,	<span class="pl-s">"Neon"</span>,	<span class="pl-c1">20.1797</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R68" data-line-number="68" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="68" data-side="right" data-line="68" data-original-line="+    [&quot;Ni&quot;,	&quot;Nickel&quot;,	58.6934]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ni"</span>,	<span class="pl-s">"Nickel"</span>,	<span class="pl-c1">58.6934</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R69" data-line-number="69" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="69" data-side="right" data-line="69" data-original-line="+    [&quot;Np&quot;,	&quot;Neptunium&quot;,	237]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Np"</span>,	<span class="pl-s">"Neptunium"</span>,	<span class="pl-c1">237</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R70" data-line-number="70" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="70" data-side="right" data-line="70" data-original-line="+    [&quot;O&quot;,	&quot;Oxygen&quot;,	15.9994]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"O"</span>,	<span class="pl-s">"Oxygen"</span>,	<span class="pl-c1">15.9994</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R71" data-line-number="71" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="71" data-side="right" data-line="71" data-original-line="+    [&quot;Os&quot;,	&quot;Osmium&quot;,	190.23]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Os"</span>,	<span class="pl-s">"Osmium"</span>,	<span class="pl-c1">190.23</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R72" data-line-number="72" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="72" data-side="right" data-line="72" data-original-line="+    [&quot;P&quot;,	&quot;Phosphorus&quot;,	30.973762]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"P"</span>,	<span class="pl-s">"Phosphorus"</span>,	<span class="pl-c1">30.973762</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R73" data-line-number="73" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="73" data-side="right" data-line="73" data-original-line="+    [&quot;Pa&quot;,	&quot;Protactinium&quot;,	231.03588]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Pa"</span>,	<span class="pl-s">"Protactinium"</span>,	<span class="pl-c1">231.03588</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R74" data-line-number="74" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="74" data-side="right" data-line="74" data-original-line="+    [&quot;Pb&quot;,	&quot;Lead&quot;,	207.2]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Pb"</span>,	<span class="pl-s">"Lead"</span>,	<span class="pl-c1">207.2</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R75" data-line-number="75" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="75" data-side="right" data-line="75" data-original-line="+    [&quot;Pd&quot;,	&quot;Palladium&quot;,	106.42]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Pd"</span>,	<span class="pl-s">"Palladium"</span>,	<span class="pl-c1">106.42</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R76" data-line-number="76" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="76" data-side="right" data-line="76" data-original-line="+    [&quot;Pm&quot;,	&quot;Promethium&quot;,	145]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Pm"</span>,	<span class="pl-s">"Promethium"</span>,	<span class="pl-c1">145</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R77" data-line-number="77" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="77" data-side="right" data-line="77" data-original-line="+    [&quot;Po&quot;,	&quot;Polonium&quot;,	209]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Po"</span>,	<span class="pl-s">"Polonium"</span>,	<span class="pl-c1">209</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R78" data-line-number="78" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="78" data-side="right" data-line="78" data-original-line="+    [&quot;Pr&quot;,	&quot;Praseodymium&quot;,	140.90765]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Pr"</span>,	<span class="pl-s">"Praseodymium"</span>,	<span class="pl-c1">140.90765</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R79" data-line-number="79" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="79" data-side="right" data-line="79" data-original-line="+    [&quot;Pt&quot;,	&quot;Platinum&quot;,	195.084]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Pt"</span>,	<span class="pl-s">"Platinum"</span>,	<span class="pl-c1">195.084</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R80" data-line-number="80" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="80" data-side="right" data-line="80" data-original-line="+    [&quot;Pu&quot;,	&quot;Plutonium&quot;,	244]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Pu"</span>,	<span class="pl-s">"Plutonium"</span>,	<span class="pl-c1">244</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R81" data-line-number="81" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="81" data-side="right" data-line="81" data-original-line="+    [&quot;Ra&quot;,	&quot;Radium&quot;,	226]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ra"</span>,	<span class="pl-s">"Radium"</span>,	<span class="pl-c1">226</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R82" data-line-number="82" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="82" data-side="right" data-line="82" data-original-line="+    [&quot;Rb&quot;,	&quot;Rubidium&quot;,	85.4678]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Rb"</span>,	<span class="pl-s">"Rubidium"</span>,	<span class="pl-c1">85.4678</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R83" data-line-number="83" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="83" data-side="right" data-line="83" data-original-line="+    [&quot;Re&quot;,	&quot;Rhenium&quot;,	186.207]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Re"</span>,	<span class="pl-s">"Rhenium"</span>,	<span class="pl-c1">186.207</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R84" data-line-number="84" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="84" data-side="right" data-line="84" data-original-line="+    [&quot;Rh&quot;,	&quot;Rhodium&quot;,	102.9055]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Rh"</span>,	<span class="pl-s">"Rhodium"</span>,	<span class="pl-c1">102.9055</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R85" data-line-number="85" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="85" data-side="right" data-line="85" data-original-line="+    [&quot;Rn&quot;,	&quot;Radon&quot;,	222]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Rn"</span>,	<span class="pl-s">"Radon"</span>,	<span class="pl-c1">222</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R86" data-line-number="86" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="86" data-side="right" data-line="86" data-original-line="+    [&quot;Ru&quot;,	&quot;Ruthenium&quot;,	101.07]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ru"</span>,	<span class="pl-s">"Ruthenium"</span>,	<span class="pl-c1">101.07</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R87" data-line-number="87" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="87" data-side="right" data-line="87" data-original-line="+    [&quot;S&quot;,	&quot;Sulfur&quot;,	32.065]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"S"</span>,	<span class="pl-s">"Sulfur"</span>,	<span class="pl-c1">32.065</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R88" data-line-number="88" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="88" data-side="right" data-line="88" data-original-line="+    [&quot;Sb&quot;,	&quot;Antimony&quot;,	121.76]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Sb"</span>,	<span class="pl-s">"Antimony"</span>,	<span class="pl-c1">121.76</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R89" data-line-number="89" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="89" data-side="right" data-line="89" data-original-line="+    [&quot;Sc&quot;,	&quot;Scandium&quot;,	44.955912]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Sc"</span>,	<span class="pl-s">"Scandium"</span>,	<span class="pl-c1">44.955912</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R90" data-line-number="90" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="90" data-side="right" data-line="90" data-original-line="+    [&quot;Se&quot;,	&quot;Selenium&quot;,	78.96]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Se"</span>,	<span class="pl-s">"Selenium"</span>,	<span class="pl-c1">78.96</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R91" data-line-number="91" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="91" data-side="right" data-line="91" data-original-line="+    [&quot;Si&quot;,	&quot;Silicon&quot;,	28.0855]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Si"</span>,	<span class="pl-s">"Silicon"</span>,	<span class="pl-c1">28.0855</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R92" data-line-number="92" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="92" data-side="right" data-line="92" data-original-line="+    [&quot;Sm&quot;,	&quot;Samarium&quot;,	150.36]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Sm"</span>,	<span class="pl-s">"Samarium"</span>,	<span class="pl-c1">150.36</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R93" data-line-number="93" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="93" data-side="right" data-line="93" data-original-line="+    [&quot;Sn&quot;,	&quot;Tin&quot;,	118.71]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Sn"</span>,	<span class="pl-s">"Tin"</span>,	<span class="pl-c1">118.71</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R94" data-line-number="94" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="94" data-side="right" data-line="94" data-original-line="+    [&quot;Sr&quot;,	&quot;Strontium&quot;,	87.62]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Sr"</span>,	<span class="pl-s">"Strontium"</span>,	<span class="pl-c1">87.62</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R95" data-line-number="95" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="95" data-side="right" data-line="95" data-original-line="+    [&quot;Ta&quot;,	&quot;Tantalum&quot;,	180.94788]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ta"</span>,	<span class="pl-s">"Tantalum"</span>,	<span class="pl-c1">180.94788</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R96" data-line-number="96" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="96" data-side="right" data-line="96" data-original-line="+    [&quot;Tb&quot;,	&quot;Terbium&quot;,	158.92535]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Tb"</span>,	<span class="pl-s">"Terbium"</span>,	<span class="pl-c1">158.92535</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R97" data-line-number="97" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="97" data-side="right" data-line="97" data-original-line="+    [&quot;Tc&quot;,	&quot;Technetium&quot;,	98]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Tc"</span>,	<span class="pl-s">"Technetium"</span>,	<span class="pl-c1">98</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R98" data-line-number="98" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="98" data-side="right" data-line="98" data-original-line="+    [&quot;Te&quot;,	&quot;Tellurium&quot;,	127.6]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Te"</span>,	<span class="pl-s">"Tellurium"</span>,	<span class="pl-c1">127.6</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R99" data-line-number="99" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="99" data-side="right" data-line="99" data-original-line="+    [&quot;Th&quot;,	&quot;Thorium&quot;,	232.03806]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Th"</span>,	<span class="pl-s">"Thorium"</span>,	<span class="pl-c1">232.03806</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R100" data-line-number="100" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="100" data-side="right" data-line="100" data-original-line="+    [&quot;Ti&quot;,	&quot;Titanium&quot;,	47.867]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Ti"</span>,	<span class="pl-s">"Titanium"</span>,	<span class="pl-c1">47.867</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R101" data-line-number="101" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="101" data-side="right" data-line="101" data-original-line="+    [&quot;Tl&quot;,	&quot;Thallium&quot;,	204.3833]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Tl"</span>,	<span class="pl-s">"Thallium"</span>,	<span class="pl-c1">204.3833</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R102" data-line-number="102" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="102" data-side="right" data-line="102" data-original-line="+    [&quot;Tm&quot;,	&quot;Thulium&quot;,	168.93421]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Tm"</span>,	<span class="pl-s">"Thulium"</span>,	<span class="pl-c1">168.93421</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R103" data-line-number="103" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="103" data-side="right" data-line="103" data-original-line="+    [&quot;U&quot;,	&quot;Uranium&quot;,	238.02891]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"U"</span>,	<span class="pl-s">"Uranium"</span>,	<span class="pl-c1">238.02891</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R104" data-line-number="104" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="104" data-side="right" data-line="104" data-original-line="+    [&quot;V&quot;,	&quot;Vanadium&quot;,	50.9415]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"V"</span>,	<span class="pl-s">"Vanadium"</span>,	<span class="pl-c1">50.9415</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R105" data-line-number="105" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="105" data-side="right" data-line="105" data-original-line="+    [&quot;W&quot;,	&quot;Tungsten&quot;,	183.84]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"W"</span>,	<span class="pl-s">"Tungsten"</span>,	<span class="pl-c1">183.84</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R106" data-line-number="106" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="106" data-side="right" data-line="106" data-original-line="+    [&quot;Xe&quot;,	&quot;Xenon&quot;,	131.293]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Xe"</span>,	<span class="pl-s">"Xenon"</span>,	<span class="pl-c1">131.293</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R107" data-line-number="107" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="107" data-side="right" data-line="107" data-original-line="+    [&quot;Y&quot;,	&quot;Yttrium&quot;,	88.90585]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Y"</span>,	<span class="pl-s">"Yttrium"</span>,	<span class="pl-c1">88.90585</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R108" data-line-number="108" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="108" data-side="right" data-line="108" data-original-line="+    [&quot;Yb&quot;,	&quot;Ytterbium&quot;,	173.054]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Yb"</span>,	<span class="pl-s">"Ytterbium"</span>,	<span class="pl-c1">173.054</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R109" data-line-number="109" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="109" data-side="right" data-line="109" data-original-line="+    [&quot;Zn&quot;,	&quot;Zinc&quot;,	65.38]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Zn"</span>,	<span class="pl-s">"Zinc"</span>,	<span class="pl-c1">65.38</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R110" data-line-number="110" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="110" data-side="right" data-line="110" data-original-line="+    [&quot;Zr&quot;,	&quot;Zirconium&quot;,	91.224]," aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    [<span class="pl-s">"Zr"</span>,	<span class="pl-s">"Zirconium"</span>,	<span class="pl-c1">91.224</span>],</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R111" data-line-number="111" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="111" data-side="right" data-line="111" data-original-line="+]" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">]</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R112" data-line-number="112" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="112" data-side="right" data-line="112" data-original-line="+    formula = &quot;&quot;" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">formula</span> <span class="pl-c1">=</span> <span class="pl-s">""</span></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R113" data-line-number="113" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="113" data-side="right" data-line="113" data-original-line="+    weight = 0" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">weight</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R114" data-line-number="114" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="114" data-side="right" data-line="114" data-original-line="+    print(f&quot;Formula: {formula} Weight: {weight}&quot;)" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">print</span>(<span class="pl-s">f"Formula: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">formula</span><span class="pl-kos">}</span></span> Weight: <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">weight</span><span class="pl-kos">}</span></span>"</span>)</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R115" data-line-number="115" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="115" data-side="right" data-line="115" data-original-line="+    return periodic_table_list" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">return</span> <span class="pl-s1">periodic_table_list</span></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R116" data-line-number="116" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="116" data-side="right" data-line="116" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R117" data-line-number="117" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="117" data-side="right" data-line="117" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R118" data-line-number="118" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="118" data-side="right" data-line="118" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R119" data-line-number="119" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="119" data-side="right" data-line="119" data-original-line="+if __name__ == &quot;__main__&quot;:" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">if</span> <span class="pl-s1">__name__</span> <span class="pl-c1">==</span> <span class="pl-s">"__main__"</span>:</span></td>
</tr>




    <tr data-hunk="37b3b145a85035376c12e80684579082b375136c2e00cc7d8d93e7e2011fe44e" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289R120" data-line-number="120" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="chemistry.py" data-anchor="diff-72c1c0f6f680d9bde5f523aa404f19b642f9eccf5d95c2a0b97313f03261d289" data-position="120" data-side="right" data-line="120" data-original-line="+    main()" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">main</span>()</span>
      <span class="no-nl-marker">
        <svg aria-label="No newline at end of file" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-no-entry">
    <path d="M4.25 7.25a.75.75 0 0 0 0 1.5h7.5a.75.75 0 0 0 0-1.5h-7.5Z"></path><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0Zm-1.5 0a6.5 6.5 0 1 0-13 0 6.5 6.5 0 0 0 13 0Z"></path>
</svg>
      </span>
    </td>
</tr>






                </tbody>
              </table>

          </div>

    </div>
  </div>
</copilot-diff-entry>

    <copilot-diff-entry data-file-path="test_chemistry_1.py">
  <div id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-details-container-group="file" class="file js-file js-details-container js-targetable-element show-inline-notes Details
               Details--on open
              
              
              
              
              
              js-tagsearch-file" data-file-type=".py" data-file-deleted="false" data-tagsearch-path="test_chemistry_1.py" data-tagsearch-lang="Python" data-targets="diff-file-filter.diffEntries">
    <div class="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch " data-path="test_chemistry_1.py" data-short-path="e1c8c65" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-file-type=".py" data-file-deleted="false">
      <div class="file-info flex-auto min-width-0 mb-md-0 mb-2">
        <button type="button" class="btn-octicon js-details-target" aria-label="Toggle diff contents" aria-expanded="true" style="width: 22px;">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down Details-content--hidden">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right Details-content--shown">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>




          <span class="sr-only">
            255 changes: 255 additions &amp; 0 deletions
          </span>
          <span class="diffstat" aria-hidden="true">255 <span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span></span>

        
<span class="Truncate">
  <a title="test_chemistry_1.py" class="Link--primary Truncate-text" href="https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13#diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5">test_chemistry_1.py</a>

  <span data-view-component="true">
  <clipboard-copy data-copy-feedback="Copied!" aria-label="Copy" value="test_chemistry_1.py" data-view-component="true" class="Link--onHover color-fg-muted ml-2 mr-2" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg style="display: none;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</clipboard-copy>  <div aria-live="polite" aria-atomic="true" class="sr-only" data-clipboard-copy-feedback=""></div>
</span>
</span>


        
      </div>

      <div class="file-actions pt-0 mb-md-0 mb-2 ml-md-2 flex-shrink-0 flex-md-justify-end">
        <div class="d-flex flex-justify-end">











          

          <details class="js-file-header-dropdown dropdown details-overlay details-reset pr-2 pl-2">
            <summary class="height-full" aria-haspopup="menu" role="button">
              <div class="height-full d-flex flex-items-center Link--secondary">
                <svg aria-label="Show options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
              </div>
            </summary>
            <details-menu class="dropdown-menu dropdown-menu-sw show-more-popover color-fg-default position-absolute f5" style="width:fit-content; min-width:185px; z-index:99; right: -4px;" role="menu" data-focus-trap="active"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
                            <label role="menuitemradio" class="dropdown-item btn-link text-normal d-block pl-5" tabindex="0" aria-checked="true">
              <span class="position-absolute ml-n4"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg></span>
              <input type="checkbox" checked="" class="d-none js-toggle-file-notes">
              Show comments
            </label>

                            <div role="none" class="dropdown-divider"></div>

                              <a href="https://github.com/mattfelber/CSE-111-programming-with-functions/blob/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13/test_chemistry_1.py" class="pl-5 dropdown-item btn-link" rel="nofollow" role="menuitem" data-ga-click="View file, click, location:files_changed_dropdown">
   View file
</a>


                                    <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to make changes.">
      Edit file
    </button>


                                  <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to delete this file.">
    Delete file
  </button>


                            <div role="none" class="dropdown-divider"></div>

                            <span data-target="copilot-diff-entry.menuItemsSlot"></span>

                
            <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
          </details>
        </div>
      </div>
    </div>


    <div class="js-file-content Details-content--hidden position-relative" data-hydro-view="{&quot;event_type&quot;:&quot;pull_request.select_diff_range&quot;,&quot;payload&quot;:{&quot;actor_id&quot;:172101276,&quot;pull_request_id&quot;:null,&quot;repository_id&quot;:null,&quot;diff_type&quot;:&quot;UNIFIED&quot;,&quot;whitespace_ignored&quot;:false,&quot;originating_url&quot;:&quot;https://github.com/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&quot;,&quot;user_id&quot;:172101276}}" data-hydro-view-hmac="2f7f8694ae5e0febe5d7308a3362e20c14b5dbb6b7f3b8f9cb0e38f3cd5e650e" data-hydro-client-context="{&quot;starting_diff_position&quot;:&quot;R1&quot;,&quot;ending_diff_position&quot;:&quot;R254&quot;,&quot;line_count&quot;:254}">


          <div class="data highlight js-blob-wrapper">
            <template class="js-file-alert-template"></template>
<template class="js-line-alert-template"></template>



              
              <table class="diff-table js-diff-table tab-size" data-tab-size="8" data-diff-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-paste-markdown-skip="">
                <thead class="sr-only">
                  <tr>
                      <th scope="col">Original file line number</th>
                      <th scope="col">Diff line number</th>
                      <th scope="col">Diff line change</th>
                  </tr>
                </thead>
                <tbody>
                      
      <tr data-position="0">
    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5HL0" class="blob-num blob-num-hunk non-expandable" data-line-number="..."></td>
    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5HR1" class="blob-num blob-num-hunk non-expandable" data-line-number="..."></td>
    <td class="blob-code blob-code-inner blob-code-hunk">@@ -0,0 +1,255 @@</td>
  </tr>

    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line selected-line-top"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R1" data-line-number="1" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line selected-line-top"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line selected-line-top">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="1" data-side="right" data-line="1" data-original-line="+# Copyright 2020, Brigham Young University-Idaho. All rights reserved." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-c"># Copyright 2020, Brigham Young University-Idaho. All rights reserved.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R2" data-line-number="2" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="2" data-side="right" data-line="2" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R3" data-line-number="3" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="3" data-side="right" data-line="3" data-original-line="+from chemistry import make_periodic_table" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">from</span> <span class="pl-s1">chemistry</span> <span class="pl-k">import</span> <span class="pl-s1">make_periodic_table</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R4" data-line-number="4" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="4" data-side="right" data-line="4" data-original-line="+from pytest import approx" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">from</span> <span class="pl-s1">pytest</span> <span class="pl-k">import</span> <span class="pl-s1">approx</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R5" data-line-number="5" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="5" data-side="right" data-line="5" data-original-line="+import pytest" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">import</span> <span class="pl-s1">pytest</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R6" data-line-number="6" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="6" data-side="right" data-line="6" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R7" data-line-number="7" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="7" data-side="right" data-line="7" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R8" data-line-number="8" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="8" data-side="right" data-line="8" data-original-line="+# These are the indexes of the" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-c"># These are the indexes of the</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R9" data-line-number="9" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="9" data-side="right" data-line="9" data-original-line="+# elements in the periodic table." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-c"># elements in the periodic table.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R10" data-line-number="10" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="10" data-side="right" data-line="10" data-original-line="+SYMBOL_INDEX = 0" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-v">SYMBOL_INDEX</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R11" data-line-number="11" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="11" data-side="right" data-line="11" data-original-line="+NAME_INDEX = 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-v">NAME_INDEX</span> <span class="pl-c1">=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R12" data-line-number="12" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="12" data-side="right" data-line="12" data-original-line="+ATOMIC_MASS_INDEX = 2" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-v">ATOMIC_MASS_INDEX</span> <span class="pl-c1">=</span> <span class="pl-c1">2</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R13" data-line-number="13" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="13" data-side="right" data-line="13" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R14" data-line-number="14" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="14" data-side="right" data-line="14" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R15" data-line-number="15" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="15" data-side="right" data-line="15" data-original-line="+def test_make_periodic_table():" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">test_make_periodic_table</span>():</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R16" data-line-number="16" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="16" data-side="right" data-line="16" data-original-line="+    &quot;&quot;&quot;Verify that the make_periodic_table function works correctly." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s">"""Verify that the make_periodic_table function works correctly.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R17" data-line-number="17" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="17" data-side="right" data-line="17" data-original-line="+    Parameters: none" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s">    Parameters: none</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R18" data-line-number="18" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="18" data-side="right" data-line="18" data-original-line="+    Return: nothing" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s">    Return: nothing</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R19" data-line-number="19" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="19" data-side="right" data-line="19" data-original-line="+    &quot;&quot;&quot;" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s">    """</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R20" data-line-number="20" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="20" data-side="right" data-line="20" data-original-line="+    # Call the make_periodic_table and store the returned" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c"># Call the make_periodic_table and store the returned</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R21" data-line-number="21" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="21" data-side="right" data-line="21" data-original-line="+    # periodic table in a variable named periodic_table_list." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c"># periodic table in a variable named periodic_table_list.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R22" data-line-number="22" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="22" data-side="right" data-line="22" data-original-line="+    periodic_table_list = make_periodic_table()" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">periodic_table_list</span> <span class="pl-c1">=</span> <span class="pl-en">make_periodic_table</span>()</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R23" data-line-number="23" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="23" data-side="right" data-line="23" data-original-line="+    assert isinstance(periodic_table_list, list), \" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">assert</span> <span class="pl-en">isinstance</span>(<span class="pl-s1">periodic_table_list</span>, <span class="pl-s1">list</span>), \</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R24" data-line-number="24" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="24" data-side="right" data-line="24" data-original-line="+        &quot;make_periodic_table function must return a list:&quot; \" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"make_periodic_table function must return a list:"</span> \</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R25" data-line-number="25" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="25" data-side="right" data-line="25" data-original-line="+        f&quot; expected a list but found a {type(periodic_table_list)}&quot;" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">f" expected a list but found a <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-en">type</span>(<span class="pl-s1">periodic_table_list</span>)<span class="pl-kos">}</span></span>"</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R26" data-line-number="26" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="26" data-side="right" data-line="26" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R27" data-line-number="27" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="27" data-side="right" data-line="27" data-original-line="+    # Create a key function that will be used by the sorted method." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c"># Create a key function that will be used by the sorted method.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R28" data-line-number="28" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="28" data-side="right" data-line="28" data-original-line="+    by_name = lambda element: element[NAME_INDEX]" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">by_name</span> <span class="pl-c1">=</span> <span class="pl-k">lambda</span> <span class="pl-s1">element</span>: <span class="pl-s1">element</span>[<span class="pl-v">NAME_INDEX</span>]</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R29" data-line-number="29" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="29" data-side="right" data-line="29" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R30" data-line-number="30" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="30" data-side="right" data-line="30" data-original-line="+    # Sort the periodic table by the element names." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c"># Sort the periodic table by the element names.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R31" data-line-number="31" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="31" data-side="right" data-line="31" data-original-line="+    periodic_table_list = sorted(periodic_table_list, key=by_name)" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">periodic_table_list</span> <span class="pl-c1">=</span> <span class="pl-en">sorted</span>(<span class="pl-s1">periodic_table_list</span>, <span class="pl-s1">key</span><span class="pl-c1">=</span><span class="pl-s1">by_name</span>)</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R32" data-line-number="32" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="32" data-side="right" data-line="32" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R33" data-line-number="33" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="33" data-side="right" data-line="33" data-original-line="+    # Check each element in the sorted periodic table." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c"># Check each element in the sorted periodic table.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R34" data-line-number="34" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="34" data-side="right" data-line="34" data-original-line="+    i = 0" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">=</span> <span class="pl-c1">0</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R35" data-line-number="35" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="35" data-side="right" data-line="35" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ac&#39;, &#39;Actinium&#39;, 227])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ac'</span>, <span class="pl-s">'Actinium'</span>, <span class="pl-c1">227</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R36" data-line-number="36" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="36" data-side="right" data-line="36" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R37" data-line-number="37" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="37" data-side="right" data-line="37" data-original-line="+    check_element(periodic_table_list[i], [&#39;Al&#39;, &#39;Aluminum&#39;, 26.9815386])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Al'</span>, <span class="pl-s">'Aluminum'</span>, <span class="pl-c1">26.9815386</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R38" data-line-number="38" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="38" data-side="right" data-line="38" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R39" data-line-number="39" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="39" data-side="right" data-line="39" data-original-line="+    check_element(periodic_table_list[i], [&#39;Sb&#39;, &#39;Antimony&#39;, 121.76])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Sb'</span>, <span class="pl-s">'Antimony'</span>, <span class="pl-c1">121.76</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R40" data-line-number="40" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="40" data-side="right" data-line="40" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R41" data-line-number="41" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="41" data-side="right" data-line="41" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ar&#39;, &#39;Argon&#39;, 39.948])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ar'</span>, <span class="pl-s">'Argon'</span>, <span class="pl-c1">39.948</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R42" data-line-number="42" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="42" data-side="right" data-line="42" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R43" data-line-number="43" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="43" data-side="right" data-line="43" data-original-line="+    check_element(periodic_table_list[i], [&#39;As&#39;, &#39;Arsenic&#39;, 74.9216])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'As'</span>, <span class="pl-s">'Arsenic'</span>, <span class="pl-c1">74.9216</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R44" data-line-number="44" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="44" data-side="right" data-line="44" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R45" data-line-number="45" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="45" data-side="right" data-line="45" data-original-line="+    check_element(periodic_table_list[i], [&#39;At&#39;, &#39;Astatine&#39;, 210])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'At'</span>, <span class="pl-s">'Astatine'</span>, <span class="pl-c1">210</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R46" data-line-number="46" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="46" data-side="right" data-line="46" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R47" data-line-number="47" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="47" data-side="right" data-line="47" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ba&#39;, &#39;Barium&#39;, 137.327])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ba'</span>, <span class="pl-s">'Barium'</span>, <span class="pl-c1">137.327</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R48" data-line-number="48" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="48" data-side="right" data-line="48" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R49" data-line-number="49" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="49" data-side="right" data-line="49" data-original-line="+    check_element(periodic_table_list[i], [&#39;Be&#39;, &#39;Beryllium&#39;, 9.012182])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Be'</span>, <span class="pl-s">'Beryllium'</span>, <span class="pl-c1">9.012182</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R50" data-line-number="50" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="50" data-side="right" data-line="50" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R51" data-line-number="51" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="51" data-side="right" data-line="51" data-original-line="+    check_element(periodic_table_list[i], [&#39;Bi&#39;, &#39;Bismuth&#39;, 208.9804])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Bi'</span>, <span class="pl-s">'Bismuth'</span>, <span class="pl-c1">208.9804</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R52" data-line-number="52" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="52" data-side="right" data-line="52" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R53" data-line-number="53" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="53" data-side="right" data-line="53" data-original-line="+    check_element(periodic_table_list[i], [&#39;B&#39;, &#39;Boron&#39;, 10.811])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'B'</span>, <span class="pl-s">'Boron'</span>, <span class="pl-c1">10.811</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R54" data-line-number="54" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="54" data-side="right" data-line="54" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R55" data-line-number="55" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="55" data-side="right" data-line="55" data-original-line="+    check_element(periodic_table_list[i], [&#39;Br&#39;, &#39;Bromine&#39;, 79.904])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Br'</span>, <span class="pl-s">'Bromine'</span>, <span class="pl-c1">79.904</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R56" data-line-number="56" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="56" data-side="right" data-line="56" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R57" data-line-number="57" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="57" data-side="right" data-line="57" data-original-line="+    check_element(periodic_table_list[i], [&#39;Cd&#39;, &#39;Cadmium&#39;, 112.411])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Cd'</span>, <span class="pl-s">'Cadmium'</span>, <span class="pl-c1">112.411</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R58" data-line-number="58" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="58" data-side="right" data-line="58" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R59" data-line-number="59" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="59" data-side="right" data-line="59" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ca&#39;, &#39;Calcium&#39;, 40.078])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ca'</span>, <span class="pl-s">'Calcium'</span>, <span class="pl-c1">40.078</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R60" data-line-number="60" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="60" data-side="right" data-line="60" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R61" data-line-number="61" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="61" data-side="right" data-line="61" data-original-line="+    check_element(periodic_table_list[i], [&#39;C&#39;, &#39;Carbon&#39;, 12.0107])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'C'</span>, <span class="pl-s">'Carbon'</span>, <span class="pl-c1">12.0107</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R62" data-line-number="62" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="62" data-side="right" data-line="62" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R63" data-line-number="63" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="63" data-side="right" data-line="63" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ce&#39;, &#39;Cerium&#39;, 140.116])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ce'</span>, <span class="pl-s">'Cerium'</span>, <span class="pl-c1">140.116</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R64" data-line-number="64" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="64" data-side="right" data-line="64" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R65" data-line-number="65" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="65" data-side="right" data-line="65" data-original-line="+    check_element(periodic_table_list[i], [&#39;Cs&#39;, &#39;Cesium&#39;, 132.9054519])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Cs'</span>, <span class="pl-s">'Cesium'</span>, <span class="pl-c1">132.9054519</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R66" data-line-number="66" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="66" data-side="right" data-line="66" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R67" data-line-number="67" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="67" data-side="right" data-line="67" data-original-line="+    check_element(periodic_table_list[i], [&#39;Cl&#39;, &#39;Chlorine&#39;, 35.453])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Cl'</span>, <span class="pl-s">'Chlorine'</span>, <span class="pl-c1">35.453</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R68" data-line-number="68" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="68" data-side="right" data-line="68" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R69" data-line-number="69" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="69" data-side="right" data-line="69" data-original-line="+    check_element(periodic_table_list[i], [&#39;Cr&#39;, &#39;Chromium&#39;, 51.9961])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Cr'</span>, <span class="pl-s">'Chromium'</span>, <span class="pl-c1">51.9961</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R70" data-line-number="70" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="70" data-side="right" data-line="70" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R71" data-line-number="71" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="71" data-side="right" data-line="71" data-original-line="+    check_element(periodic_table_list[i], [&#39;Co&#39;, &#39;Cobalt&#39;, 58.933195])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Co'</span>, <span class="pl-s">'Cobalt'</span>, <span class="pl-c1">58.933195</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R72" data-line-number="72" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="72" data-side="right" data-line="72" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R73" data-line-number="73" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="73" data-side="right" data-line="73" data-original-line="+    check_element(periodic_table_list[i], [&#39;Cu&#39;, &#39;Copper&#39;, 63.546])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Cu'</span>, <span class="pl-s">'Copper'</span>, <span class="pl-c1">63.546</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R74" data-line-number="74" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="74" data-side="right" data-line="74" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R75" data-line-number="75" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="75" data-side="right" data-line="75" data-original-line="+    check_element(periodic_table_list[i], [&#39;Dy&#39;, &#39;Dysprosium&#39;, 162.5])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Dy'</span>, <span class="pl-s">'Dysprosium'</span>, <span class="pl-c1">162.5</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R76" data-line-number="76" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="76" data-side="right" data-line="76" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R77" data-line-number="77" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="77" data-side="right" data-line="77" data-original-line="+    check_element(periodic_table_list[i], [&#39;Er&#39;, &#39;Erbium&#39;, 167.259])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Er'</span>, <span class="pl-s">'Erbium'</span>, <span class="pl-c1">167.259</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R78" data-line-number="78" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="78" data-side="right" data-line="78" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R79" data-line-number="79" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="79" data-side="right" data-line="79" data-original-line="+    check_element(periodic_table_list[i], [&#39;Eu&#39;, &#39;Europium&#39;, 151.964])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Eu'</span>, <span class="pl-s">'Europium'</span>, <span class="pl-c1">151.964</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R80" data-line-number="80" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="80" data-side="right" data-line="80" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R81" data-line-number="81" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="81" data-side="right" data-line="81" data-original-line="+    check_element(periodic_table_list[i], [&#39;F&#39;, &#39;Fluorine&#39;, 18.9984032])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'F'</span>, <span class="pl-s">'Fluorine'</span>, <span class="pl-c1">18.9984032</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R82" data-line-number="82" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="82" data-side="right" data-line="82" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R83" data-line-number="83" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="83" data-side="right" data-line="83" data-original-line="+    check_element(periodic_table_list[i], [&#39;Fr&#39;, &#39;Francium&#39;, 223])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Fr'</span>, <span class="pl-s">'Francium'</span>, <span class="pl-c1">223</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R84" data-line-number="84" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="84" data-side="right" data-line="84" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R85" data-line-number="85" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="85" data-side="right" data-line="85" data-original-line="+    check_element(periodic_table_list[i], [&#39;Gd&#39;, &#39;Gadolinium&#39;, 157.25])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Gd'</span>, <span class="pl-s">'Gadolinium'</span>, <span class="pl-c1">157.25</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R86" data-line-number="86" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="86" data-side="right" data-line="86" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R87" data-line-number="87" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="87" data-side="right" data-line="87" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ga&#39;, &#39;Gallium&#39;, 69.723])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ga'</span>, <span class="pl-s">'Gallium'</span>, <span class="pl-c1">69.723</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R88" data-line-number="88" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="88" data-side="right" data-line="88" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R89" data-line-number="89" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="89" data-side="right" data-line="89" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ge&#39;, &#39;Germanium&#39;, 72.64])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ge'</span>, <span class="pl-s">'Germanium'</span>, <span class="pl-c1">72.64</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R90" data-line-number="90" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="90" data-side="right" data-line="90" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R91" data-line-number="91" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="91" data-side="right" data-line="91" data-original-line="+    check_element(periodic_table_list[i], [&#39;Au&#39;, &#39;Gold&#39;, 196.966569])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Au'</span>, <span class="pl-s">'Gold'</span>, <span class="pl-c1">196.966569</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R92" data-line-number="92" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="92" data-side="right" data-line="92" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R93" data-line-number="93" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="93" data-side="right" data-line="93" data-original-line="+    check_element(periodic_table_list[i], [&#39;Hf&#39;, &#39;Hafnium&#39;, 178.49])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Hf'</span>, <span class="pl-s">'Hafnium'</span>, <span class="pl-c1">178.49</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R94" data-line-number="94" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="94" data-side="right" data-line="94" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R95" data-line-number="95" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="95" data-side="right" data-line="95" data-original-line="+    check_element(periodic_table_list[i], [&#39;He&#39;, &#39;Helium&#39;, 4.002602])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'He'</span>, <span class="pl-s">'Helium'</span>, <span class="pl-c1">4.002602</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R96" data-line-number="96" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="96" data-side="right" data-line="96" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R97" data-line-number="97" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="97" data-side="right" data-line="97" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ho&#39;, &#39;Holmium&#39;, 164.93032])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ho'</span>, <span class="pl-s">'Holmium'</span>, <span class="pl-c1">164.93032</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R98" data-line-number="98" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="98" data-side="right" data-line="98" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R99" data-line-number="99" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="99" data-side="right" data-line="99" data-original-line="+    check_element(periodic_table_list[i], [&#39;H&#39;, &#39;Hydrogen&#39;, 1.00794])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'H'</span>, <span class="pl-s">'Hydrogen'</span>, <span class="pl-c1">1.00794</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R100" data-line-number="100" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="100" data-side="right" data-line="100" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R101" data-line-number="101" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="101" data-side="right" data-line="101" data-original-line="+    check_element(periodic_table_list[i], [&#39;In&#39;, &#39;Indium&#39;, 114.818])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'In'</span>, <span class="pl-s">'Indium'</span>, <span class="pl-c1">114.818</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R102" data-line-number="102" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="102" data-side="right" data-line="102" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R103" data-line-number="103" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="103" data-side="right" data-line="103" data-original-line="+    check_element(periodic_table_list[i], [&#39;I&#39;, &#39;Iodine&#39;, 126.90447])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'I'</span>, <span class="pl-s">'Iodine'</span>, <span class="pl-c1">126.90447</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R104" data-line-number="104" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="104" data-side="right" data-line="104" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R105" data-line-number="105" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="105" data-side="right" data-line="105" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ir&#39;, &#39;Iridium&#39;, 192.217])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ir'</span>, <span class="pl-s">'Iridium'</span>, <span class="pl-c1">192.217</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R106" data-line-number="106" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="106" data-side="right" data-line="106" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R107" data-line-number="107" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="107" data-side="right" data-line="107" data-original-line="+    check_element(periodic_table_list[i], [&#39;Fe&#39;, &#39;Iron&#39;, 55.845])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Fe'</span>, <span class="pl-s">'Iron'</span>, <span class="pl-c1">55.845</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R108" data-line-number="108" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="108" data-side="right" data-line="108" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R109" data-line-number="109" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="109" data-side="right" data-line="109" data-original-line="+    check_element(periodic_table_list[i], [&#39;Kr&#39;, &#39;Krypton&#39;, 83.798])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Kr'</span>, <span class="pl-s">'Krypton'</span>, <span class="pl-c1">83.798</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R110" data-line-number="110" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="110" data-side="right" data-line="110" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R111" data-line-number="111" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="111" data-side="right" data-line="111" data-original-line="+    check_element(periodic_table_list[i], [&#39;La&#39;, &#39;Lanthanum&#39;, 138.90547])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'La'</span>, <span class="pl-s">'Lanthanum'</span>, <span class="pl-c1">138.90547</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R112" data-line-number="112" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="112" data-side="right" data-line="112" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R113" data-line-number="113" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="113" data-side="right" data-line="113" data-original-line="+    check_element(periodic_table_list[i], [&#39;Pb&#39;, &#39;Lead&#39;, 207.2])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Pb'</span>, <span class="pl-s">'Lead'</span>, <span class="pl-c1">207.2</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R114" data-line-number="114" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="114" data-side="right" data-line="114" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R115" data-line-number="115" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="115" data-side="right" data-line="115" data-original-line="+    check_element(periodic_table_list[i], [&#39;Li&#39;, &#39;Lithium&#39;, 6.941])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Li'</span>, <span class="pl-s">'Lithium'</span>, <span class="pl-c1">6.941</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R116" data-line-number="116" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="116" data-side="right" data-line="116" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R117" data-line-number="117" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="117" data-side="right" data-line="117" data-original-line="+    check_element(periodic_table_list[i], [&#39;Lu&#39;, &#39;Lutetium&#39;, 174.9668])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Lu'</span>, <span class="pl-s">'Lutetium'</span>, <span class="pl-c1">174.9668</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R118" data-line-number="118" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="118" data-side="right" data-line="118" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R119" data-line-number="119" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="119" data-side="right" data-line="119" data-original-line="+    check_element(periodic_table_list[i], [&#39;Mg&#39;, &#39;Magnesium&#39;, 24.305])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Mg'</span>, <span class="pl-s">'Magnesium'</span>, <span class="pl-c1">24.305</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R120" data-line-number="120" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="120" data-side="right" data-line="120" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R121" data-line-number="121" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="121" data-side="right" data-line="121" data-original-line="+    check_element(periodic_table_list[i], [&#39;Mn&#39;, &#39;Manganese&#39;, 54.938045])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Mn'</span>, <span class="pl-s">'Manganese'</span>, <span class="pl-c1">54.938045</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R122" data-line-number="122" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="122" data-side="right" data-line="122" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R123" data-line-number="123" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="123" data-side="right" data-line="123" data-original-line="+    check_element(periodic_table_list[i], [&#39;Hg&#39;, &#39;Mercury&#39;, 200.59])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Hg'</span>, <span class="pl-s">'Mercury'</span>, <span class="pl-c1">200.59</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R124" data-line-number="124" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="124" data-side="right" data-line="124" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R125" data-line-number="125" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="125" data-side="right" data-line="125" data-original-line="+    check_element(periodic_table_list[i], [&#39;Mo&#39;, &#39;Molybdenum&#39;, 95.96])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Mo'</span>, <span class="pl-s">'Molybdenum'</span>, <span class="pl-c1">95.96</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R126" data-line-number="126" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="126" data-side="right" data-line="126" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R127" data-line-number="127" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="127" data-side="right" data-line="127" data-original-line="+    check_element(periodic_table_list[i], [&#39;Nd&#39;, &#39;Neodymium&#39;, 144.242])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Nd'</span>, <span class="pl-s">'Neodymium'</span>, <span class="pl-c1">144.242</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R128" data-line-number="128" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="128" data-side="right" data-line="128" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R129" data-line-number="129" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="129" data-side="right" data-line="129" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ne&#39;, &#39;Neon&#39;, 20.1797])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ne'</span>, <span class="pl-s">'Neon'</span>, <span class="pl-c1">20.1797</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R130" data-line-number="130" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="130" data-side="right" data-line="130" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R131" data-line-number="131" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="131" data-side="right" data-line="131" data-original-line="+    check_element(periodic_table_list[i], [&#39;Np&#39;, &#39;Neptunium&#39;, 237])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Np'</span>, <span class="pl-s">'Neptunium'</span>, <span class="pl-c1">237</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R132" data-line-number="132" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="132" data-side="right" data-line="132" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R133" data-line-number="133" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="133" data-side="right" data-line="133" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ni&#39;, &#39;Nickel&#39;, 58.6934])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ni'</span>, <span class="pl-s">'Nickel'</span>, <span class="pl-c1">58.6934</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R134" data-line-number="134" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="134" data-side="right" data-line="134" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R135" data-line-number="135" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="135" data-side="right" data-line="135" data-original-line="+    check_element(periodic_table_list[i], [&#39;Nb&#39;, &#39;Niobium&#39;, 92.90638])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Nb'</span>, <span class="pl-s">'Niobium'</span>, <span class="pl-c1">92.90638</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R136" data-line-number="136" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="136" data-side="right" data-line="136" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R137" data-line-number="137" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="137" data-side="right" data-line="137" data-original-line="+    check_element(periodic_table_list[i], [&#39;N&#39;, &#39;Nitrogen&#39;, 14.0067])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'N'</span>, <span class="pl-s">'Nitrogen'</span>, <span class="pl-c1">14.0067</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R138" data-line-number="138" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="138" data-side="right" data-line="138" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R139" data-line-number="139" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="139" data-side="right" data-line="139" data-original-line="+    check_element(periodic_table_list[i], [&#39;Os&#39;, &#39;Osmium&#39;, 190.23])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Os'</span>, <span class="pl-s">'Osmium'</span>, <span class="pl-c1">190.23</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R140" data-line-number="140" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="140" data-side="right" data-line="140" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R141" data-line-number="141" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="141" data-side="right" data-line="141" data-original-line="+    check_element(periodic_table_list[i], [&#39;O&#39;, &#39;Oxygen&#39;, 15.9994])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'O'</span>, <span class="pl-s">'Oxygen'</span>, <span class="pl-c1">15.9994</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R142" data-line-number="142" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="142" data-side="right" data-line="142" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R143" data-line-number="143" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="143" data-side="right" data-line="143" data-original-line="+    check_element(periodic_table_list[i], [&#39;Pd&#39;, &#39;Palladium&#39;, 106.42])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Pd'</span>, <span class="pl-s">'Palladium'</span>, <span class="pl-c1">106.42</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R144" data-line-number="144" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="144" data-side="right" data-line="144" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R145" data-line-number="145" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="145" data-side="right" data-line="145" data-original-line="+    check_element(periodic_table_list[i], [&#39;P&#39;, &#39;Phosphorus&#39;, 30.973762])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'P'</span>, <span class="pl-s">'Phosphorus'</span>, <span class="pl-c1">30.973762</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R146" data-line-number="146" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="146" data-side="right" data-line="146" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R147" data-line-number="147" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="147" data-side="right" data-line="147" data-original-line="+    check_element(periodic_table_list[i], [&#39;Pt&#39;, &#39;Platinum&#39;, 195.084])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Pt'</span>, <span class="pl-s">'Platinum'</span>, <span class="pl-c1">195.084</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R148" data-line-number="148" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="148" data-side="right" data-line="148" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R149" data-line-number="149" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="149" data-side="right" data-line="149" data-original-line="+    check_element(periodic_table_list[i], [&#39;Pu&#39;, &#39;Plutonium&#39;, 244])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Pu'</span>, <span class="pl-s">'Plutonium'</span>, <span class="pl-c1">244</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R150" data-line-number="150" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="150" data-side="right" data-line="150" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R151" data-line-number="151" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="151" data-side="right" data-line="151" data-original-line="+    check_element(periodic_table_list[i], [&#39;Po&#39;, &#39;Polonium&#39;, 209])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Po'</span>, <span class="pl-s">'Polonium'</span>, <span class="pl-c1">209</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R152" data-line-number="152" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="152" data-side="right" data-line="152" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R153" data-line-number="153" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="153" data-side="right" data-line="153" data-original-line="+    check_element(periodic_table_list[i], [&#39;K&#39;, &#39;Potassium&#39;, 39.0983])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'K'</span>, <span class="pl-s">'Potassium'</span>, <span class="pl-c1">39.0983</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R154" data-line-number="154" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="154" data-side="right" data-line="154" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R155" data-line-number="155" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="155" data-side="right" data-line="155" data-original-line="+    check_element(periodic_table_list[i], [&#39;Pr&#39;, &#39;Praseodymium&#39;, 140.90765])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Pr'</span>, <span class="pl-s">'Praseodymium'</span>, <span class="pl-c1">140.90765</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R156" data-line-number="156" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="156" data-side="right" data-line="156" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R157" data-line-number="157" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="157" data-side="right" data-line="157" data-original-line="+    check_element(periodic_table_list[i], [&#39;Pm&#39;, &#39;Promethium&#39;, 145])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Pm'</span>, <span class="pl-s">'Promethium'</span>, <span class="pl-c1">145</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R158" data-line-number="158" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="158" data-side="right" data-line="158" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R159" data-line-number="159" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="159" data-side="right" data-line="159" data-original-line="+    check_element(periodic_table_list[i], [&#39;Pa&#39;, &#39;Protactinium&#39;, 231.03588])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Pa'</span>, <span class="pl-s">'Protactinium'</span>, <span class="pl-c1">231.03588</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R160" data-line-number="160" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="160" data-side="right" data-line="160" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R161" data-line-number="161" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="161" data-side="right" data-line="161" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ra&#39;, &#39;Radium&#39;, 226])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ra'</span>, <span class="pl-s">'Radium'</span>, <span class="pl-c1">226</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R162" data-line-number="162" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="162" data-side="right" data-line="162" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R163" data-line-number="163" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="163" data-side="right" data-line="163" data-original-line="+    check_element(periodic_table_list[i], [&#39;Rn&#39;, &#39;Radon&#39;, 222])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Rn'</span>, <span class="pl-s">'Radon'</span>, <span class="pl-c1">222</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R164" data-line-number="164" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="164" data-side="right" data-line="164" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R165" data-line-number="165" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="165" data-side="right" data-line="165" data-original-line="+    check_element(periodic_table_list[i], [&#39;Re&#39;, &#39;Rhenium&#39;, 186.207])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Re'</span>, <span class="pl-s">'Rhenium'</span>, <span class="pl-c1">186.207</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R166" data-line-number="166" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="166" data-side="right" data-line="166" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R167" data-line-number="167" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="167" data-side="right" data-line="167" data-original-line="+    check_element(periodic_table_list[i], [&#39;Rh&#39;, &#39;Rhodium&#39;, 102.9055])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Rh'</span>, <span class="pl-s">'Rhodium'</span>, <span class="pl-c1">102.9055</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R168" data-line-number="168" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="168" data-side="right" data-line="168" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R169" data-line-number="169" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="169" data-side="right" data-line="169" data-original-line="+    check_element(periodic_table_list[i], [&#39;Rb&#39;, &#39;Rubidium&#39;, 85.4678])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Rb'</span>, <span class="pl-s">'Rubidium'</span>, <span class="pl-c1">85.4678</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R170" data-line-number="170" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="170" data-side="right" data-line="170" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R171" data-line-number="171" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="171" data-side="right" data-line="171" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ru&#39;, &#39;Ruthenium&#39;, 101.07])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ru'</span>, <span class="pl-s">'Ruthenium'</span>, <span class="pl-c1">101.07</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R172" data-line-number="172" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="172" data-side="right" data-line="172" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R173" data-line-number="173" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="173" data-side="right" data-line="173" data-original-line="+    check_element(periodic_table_list[i], [&#39;Sm&#39;, &#39;Samarium&#39;, 150.36])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Sm'</span>, <span class="pl-s">'Samarium'</span>, <span class="pl-c1">150.36</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R174" data-line-number="174" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="174" data-side="right" data-line="174" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R175" data-line-number="175" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="175" data-side="right" data-line="175" data-original-line="+    check_element(periodic_table_list[i], [&#39;Sc&#39;, &#39;Scandium&#39;, 44.955912])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Sc'</span>, <span class="pl-s">'Scandium'</span>, <span class="pl-c1">44.955912</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R176" data-line-number="176" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="176" data-side="right" data-line="176" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R177" data-line-number="177" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="177" data-side="right" data-line="177" data-original-line="+    check_element(periodic_table_list[i], [&#39;Se&#39;, &#39;Selenium&#39;, 78.96])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Se'</span>, <span class="pl-s">'Selenium'</span>, <span class="pl-c1">78.96</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R178" data-line-number="178" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="178" data-side="right" data-line="178" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R179" data-line-number="179" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="179" data-side="right" data-line="179" data-original-line="+    check_element(periodic_table_list[i], [&#39;Si&#39;, &#39;Silicon&#39;, 28.0855])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Si'</span>, <span class="pl-s">'Silicon'</span>, <span class="pl-c1">28.0855</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R180" data-line-number="180" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="180" data-side="right" data-line="180" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R181" data-line-number="181" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="181" data-side="right" data-line="181" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ag&#39;, &#39;Silver&#39;, 107.8682])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ag'</span>, <span class="pl-s">'Silver'</span>, <span class="pl-c1">107.8682</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R182" data-line-number="182" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="182" data-side="right" data-line="182" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R183" data-line-number="183" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="183" data-side="right" data-line="183" data-original-line="+    check_element(periodic_table_list[i], [&#39;Na&#39;, &#39;Sodium&#39;, 22.98976928])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Na'</span>, <span class="pl-s">'Sodium'</span>, <span class="pl-c1">22.98976928</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R184" data-line-number="184" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="184" data-side="right" data-line="184" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R185" data-line-number="185" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="185" data-side="right" data-line="185" data-original-line="+    check_element(periodic_table_list[i], [&#39;Sr&#39;, &#39;Strontium&#39;, 87.62])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Sr'</span>, <span class="pl-s">'Strontium'</span>, <span class="pl-c1">87.62</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R186" data-line-number="186" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="186" data-side="right" data-line="186" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R187" data-line-number="187" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="187" data-side="right" data-line="187" data-original-line="+    check_element(periodic_table_list[i], [&#39;S&#39;, &#39;Sulfur&#39;, 32.065])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'S'</span>, <span class="pl-s">'Sulfur'</span>, <span class="pl-c1">32.065</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R188" data-line-number="188" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="188" data-side="right" data-line="188" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R189" data-line-number="189" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="189" data-side="right" data-line="189" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ta&#39;, &#39;Tantalum&#39;, 180.94788])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ta'</span>, <span class="pl-s">'Tantalum'</span>, <span class="pl-c1">180.94788</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R190" data-line-number="190" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="190" data-side="right" data-line="190" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R191" data-line-number="191" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="191" data-side="right" data-line="191" data-original-line="+    check_element(periodic_table_list[i], [&#39;Tc&#39;, &#39;Technetium&#39;, 98])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Tc'</span>, <span class="pl-s">'Technetium'</span>, <span class="pl-c1">98</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R192" data-line-number="192" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="192" data-side="right" data-line="192" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R193" data-line-number="193" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="193" data-side="right" data-line="193" data-original-line="+    check_element(periodic_table_list[i], [&#39;Te&#39;, &#39;Tellurium&#39;, 127.6])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Te'</span>, <span class="pl-s">'Tellurium'</span>, <span class="pl-c1">127.6</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R194" data-line-number="194" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="194" data-side="right" data-line="194" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R195" data-line-number="195" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="195" data-side="right" data-line="195" data-original-line="+    check_element(periodic_table_list[i], [&#39;Tb&#39;, &#39;Terbium&#39;, 158.92535])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Tb'</span>, <span class="pl-s">'Terbium'</span>, <span class="pl-c1">158.92535</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R196" data-line-number="196" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="196" data-side="right" data-line="196" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R197" data-line-number="197" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="197" data-side="right" data-line="197" data-original-line="+    check_element(periodic_table_list[i], [&#39;Tl&#39;, &#39;Thallium&#39;, 204.3833])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Tl'</span>, <span class="pl-s">'Thallium'</span>, <span class="pl-c1">204.3833</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R198" data-line-number="198" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="198" data-side="right" data-line="198" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R199" data-line-number="199" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="199" data-side="right" data-line="199" data-original-line="+    check_element(periodic_table_list[i], [&#39;Th&#39;, &#39;Thorium&#39;, 232.03806])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Th'</span>, <span class="pl-s">'Thorium'</span>, <span class="pl-c1">232.03806</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R200" data-line-number="200" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="200" data-side="right" data-line="200" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R201" data-line-number="201" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="201" data-side="right" data-line="201" data-original-line="+    check_element(periodic_table_list[i], [&#39;Tm&#39;, &#39;Thulium&#39;, 168.93421])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Tm'</span>, <span class="pl-s">'Thulium'</span>, <span class="pl-c1">168.93421</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R202" data-line-number="202" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="202" data-side="right" data-line="202" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R203" data-line-number="203" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="203" data-side="right" data-line="203" data-original-line="+    check_element(periodic_table_list[i], [&#39;Sn&#39;, &#39;Tin&#39;, 118.71])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Sn'</span>, <span class="pl-s">'Tin'</span>, <span class="pl-c1">118.71</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R204" data-line-number="204" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="204" data-side="right" data-line="204" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R205" data-line-number="205" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="205" data-side="right" data-line="205" data-original-line="+    check_element(periodic_table_list[i], [&#39;Ti&#39;, &#39;Titanium&#39;, 47.867])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Ti'</span>, <span class="pl-s">'Titanium'</span>, <span class="pl-c1">47.867</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R206" data-line-number="206" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="206" data-side="right" data-line="206" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R207" data-line-number="207" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="207" data-side="right" data-line="207" data-original-line="+    check_element(periodic_table_list[i], [&#39;W&#39;, &#39;Tungsten&#39;, 183.84])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'W'</span>, <span class="pl-s">'Tungsten'</span>, <span class="pl-c1">183.84</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R208" data-line-number="208" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="208" data-side="right" data-line="208" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R209" data-line-number="209" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="209" data-side="right" data-line="209" data-original-line="+    check_element(periodic_table_list[i], [&#39;U&#39;, &#39;Uranium&#39;, 238.02891])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'U'</span>, <span class="pl-s">'Uranium'</span>, <span class="pl-c1">238.02891</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R210" data-line-number="210" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="210" data-side="right" data-line="210" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R211" data-line-number="211" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="211" data-side="right" data-line="211" data-original-line="+    check_element(periodic_table_list[i], [&#39;V&#39;, &#39;Vanadium&#39;, 50.9415])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'V'</span>, <span class="pl-s">'Vanadium'</span>, <span class="pl-c1">50.9415</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R212" data-line-number="212" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="212" data-side="right" data-line="212" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R213" data-line-number="213" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="213" data-side="right" data-line="213" data-original-line="+    check_element(periodic_table_list[i], [&#39;Xe&#39;, &#39;Xenon&#39;, 131.293])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Xe'</span>, <span class="pl-s">'Xenon'</span>, <span class="pl-c1">131.293</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R214" data-line-number="214" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="214" data-side="right" data-line="214" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R215" data-line-number="215" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="215" data-side="right" data-line="215" data-original-line="+    check_element(periodic_table_list[i], [&#39;Yb&#39;, &#39;Ytterbium&#39;, 173.054])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Yb'</span>, <span class="pl-s">'Ytterbium'</span>, <span class="pl-c1">173.054</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R216" data-line-number="216" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="216" data-side="right" data-line="216" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R217" data-line-number="217" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="217" data-side="right" data-line="217" data-original-line="+    check_element(periodic_table_list[i], [&#39;Y&#39;, &#39;Yttrium&#39;, 88.90585])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Y'</span>, <span class="pl-s">'Yttrium'</span>, <span class="pl-c1">88.90585</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R218" data-line-number="218" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="218" data-side="right" data-line="218" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R219" data-line-number="219" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="219" data-side="right" data-line="219" data-original-line="+    check_element(periodic_table_list[i], [&#39;Zn&#39;, &#39;Zinc&#39;, 65.38])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Zn'</span>, <span class="pl-s">'Zinc'</span>, <span class="pl-c1">65.38</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R220" data-line-number="220" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="220" data-side="right" data-line="220" data-original-line="+    i += 1" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">i</span> <span class="pl-c1">+=</span> <span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R221" data-line-number="221" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="221" data-side="right" data-line="221" data-original-line="+    check_element(periodic_table_list[i], [&#39;Zr&#39;, &#39;Zirconium&#39;, 91.224])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-en">check_element</span>(<span class="pl-s1">periodic_table_list</span>[<span class="pl-s1">i</span>], [<span class="pl-s">'Zr'</span>, <span class="pl-s">'Zirconium'</span>, <span class="pl-c1">91.224</span>])</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R222" data-line-number="222" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="222" data-side="right" data-line="222" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R223" data-line-number="223" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="223" data-side="right" data-line="223" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R224" data-line-number="224" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="224" data-side="right" data-line="224" data-original-line="+def check_element(actual, expected):" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">check_element</span>(<span class="pl-s1">actual</span>, <span class="pl-s1">expected</span>):</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R225" data-line-number="225" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="225" data-side="right" data-line="225" data-original-line="+    &quot;&quot;&quot;Verify that the actual element that came from the" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s">"""Verify that the actual element that came from the</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R226" data-line-number="226" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="226" data-side="right" data-line="226" data-original-line="+    periodic_table_list contains the same values as the" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s">    periodic_table_list contains the same values as the</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R227" data-line-number="227" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="227" data-side="right" data-line="227" data-original-line="+    expected element." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s">    expected element.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R228" data-line-number="228" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="228" data-side="right" data-line="228" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s"></span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R229" data-line-number="229" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="229" data-side="right" data-line="229" data-original-line="+    Parameters" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s">    Parameters</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R230" data-line-number="230" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="230" data-side="right" data-line="230" data-original-line="+        actual: a list that came from the periodic_table_list." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s">        actual: a list that came from the periodic_table_list.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R231" data-line-number="231" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="231" data-side="right" data-line="231" data-original-line="+        expected: a list that contains the expected values." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s">        expected: a list that contains the expected values.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R232" data-line-number="232" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="232" data-side="right" data-line="232" data-original-line="+    Return: nothing" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s">    Return: nothing</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R233" data-line-number="233" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="233" data-side="right" data-line="233" data-original-line="+    &quot;&quot;&quot;" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s">    """</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R234" data-line-number="234" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="234" data-side="right" data-line="234" data-original-line="+    name = expected[NAME_INDEX]" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">name</span> <span class="pl-c1">=</span> <span class="pl-s1">expected</span>[<span class="pl-v">NAME_INDEX</span>]</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R235" data-line-number="235" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="235" data-side="right" data-line="235" data-original-line="+    assert actual[NAME_INDEX] == name, \" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">assert</span> <span class="pl-s1">actual</span>[<span class="pl-v">NAME_INDEX</span>] <span class="pl-c1">==</span> <span class="pl-s1">name</span>, \</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R236" data-line-number="236" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="236" data-side="right" data-line="236" data-original-line="+         f&quot;{name} is missing from the periodic table.&quot;" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">         <span class="pl-s">f"<span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">name</span><span class="pl-kos">}</span></span> is missing from the periodic table."</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R237" data-line-number="237" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="237" data-side="right" data-line="237" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R238" data-line-number="238" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="238" data-side="right" data-line="238" data-original-line="+    # Verify that the element&#39;s symbol is correct." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c"># Verify that the element's symbol is correct.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R239" data-line-number="239" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="239" data-side="right" data-line="239" data-original-line="+    act_symbol = actual[SYMBOL_INDEX]" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">act_symbol</span> <span class="pl-c1">=</span> <span class="pl-s1">actual</span>[<span class="pl-v">SYMBOL_INDEX</span>]</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R240" data-line-number="240" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="240" data-side="right" data-line="240" data-original-line="+    exp_symbol = expected[SYMBOL_INDEX]" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">exp_symbol</span> <span class="pl-c1">=</span> <span class="pl-s1">expected</span>[<span class="pl-v">SYMBOL_INDEX</span>]</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R241" data-line-number="241" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="241" data-side="right" data-line="241" data-original-line="+    assert act_symbol == exp_symbol, \" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">assert</span> <span class="pl-s1">act_symbol</span> <span class="pl-c1">==</span> <span class="pl-s1">exp_symbol</span>, \</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R242" data-line-number="242" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="242" data-side="right" data-line="242" data-original-line="+         f&quot;wrong symbol for {name}: &quot; \" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">         <span class="pl-s">f"wrong symbol for <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">name</span><span class="pl-kos">}</span></span>: "</span> \</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R243" data-line-number="243" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="243" data-side="right" data-line="243" data-original-line="+         f&quot;expected {exp_symbol} but found {act_symbol}.&quot;" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">         <span class="pl-s">f"expected <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">exp_symbol</span><span class="pl-kos">}</span></span> but found <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">act_symbol</span><span class="pl-kos">}</span></span>."</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R244" data-line-number="244" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="244" data-side="right" data-line="244" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R245" data-line-number="245" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="245" data-side="right" data-line="245" data-original-line="+    # Verify that the element&#39;s atomic mass is correct." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c"># Verify that the element's atomic mass is correct.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R246" data-line-number="246" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="246" data-side="right" data-line="246" data-original-line="+    act_mass = actual[ATOMIC_MASS_INDEX]" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">act_mass</span> <span class="pl-c1">=</span> <span class="pl-s1">actual</span>[<span class="pl-v">ATOMIC_MASS_INDEX</span>]</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R247" data-line-number="247" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="247" data-side="right" data-line="247" data-original-line="+    exp_mass = expected[ATOMIC_MASS_INDEX]" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">exp_mass</span> <span class="pl-c1">=</span> <span class="pl-s1">expected</span>[<span class="pl-v">ATOMIC_MASS_INDEX</span>]</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R248" data-line-number="248" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="248" data-side="right" data-line="248" data-original-line="+    assert act_mass == approx(exp_mass), \" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">assert</span> <span class="pl-s1">act_mass</span> <span class="pl-c1">==</span> <span class="pl-en">approx</span>(<span class="pl-s1">exp_mass</span>), \</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R249" data-line-number="249" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="249" data-side="right" data-line="249" data-original-line="+            f&quot;wrong atomic mass for {name}: &quot; \" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">            <span class="pl-s">f"wrong atomic mass for <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">name</span><span class="pl-kos">}</span></span>: "</span> \</span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R250" data-line-number="250" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="250" data-side="right" data-line="250" data-original-line="+            f&quot;expected {exp_mass} but found {act_mass}&quot;" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">            <span class="pl-s">f"expected <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">exp_mass</span><span class="pl-kos">}</span></span> but found <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">act_mass</span><span class="pl-kos">}</span></span>"</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R251" data-line-number="251" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="251" data-side="right" data-line="251" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R252" data-line-number="252" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="252" data-side="right" data-line="252" data-original-line="+" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R253" data-line-number="253" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="253" data-side="right" data-line="253" data-original-line="+# Call the main function that is part of pytest so that the" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-c"># Call the main function that is part of pytest so that the</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell selected-line selected-line-bottom"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R254" data-line-number="254" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum selected-line selected-line-bottom"></td>

  <td class="blob-code blob-code-addition js-file-line selected-line selected-line-bottom">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="254" data-side="right" data-line="254" data-original-line="+# computer will execute the test functions in this file." aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-c"># computer will execute the test functions in this file.</span></span></td>
</tr>




    <tr data-hunk="8bce876a9a739ac9361405d8fc4bdb2a6965c09370e780a63e6186f1e661a0d8" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5R255" data-line-number="255" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="test_chemistry_1.py" data-anchor="diff-e1c8c652f21cfc1168cebc3b073f147d43270a7f7c8a150547bbdbefd8bc0dd5" data-position="255" data-side="right" data-line="255" data-original-line="+pytest.main([&quot;-v&quot;, &quot;--tb=line&quot;, &quot;-rN&quot;, __file__])" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s1">pytest</span>.<span class="pl-en">main</span>([<span class="pl-s">"-v"</span>, <span class="pl-s">"--tb=line"</span>, <span class="pl-s">"-rN"</span>, <span class="pl-s1">__file__</span>])</span></td>
</tr>






                </tbody>
              </table>

          </div>

    </div>
  </div>
</copilot-diff-entry>

  </div>


</div>

<button type="button" class="js-toggle-all-file-notes" data-hotkey="i" style="display:none">Toggle all file notes</button>

<button type="button" class="js-toggle-all-file-annotations" data-hotkey="a" style="display:none">Toggle all file annotations</button>

<svg aria-hidden="true" width="100px" height="84px" viewBox="0 0 340 84" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="diff-placeholder-svg position-absolute bottom-0">
  <defs>
    <clippath id="diff-placeholder">
      <rect x="0" y="0" width="67.0175439" height="11.9298746" rx="2"></rect>
      <rect x="18.9473684" y="47.7194983" width="100.701754" height="11.9298746" rx="2"></rect>
      <rect x="0" y="71.930126" width="37.8947368" height="11.9298746" rx="2"></rect>
      <rect x="127.017544" y="48.0703769" width="53.3333333" height="11.9298746" rx="2"></rect>
      <rect x="187.719298" y="48.0703769" width="72.9824561" height="11.9298746" rx="2"></rect>
      <rect x="76.8421053" y="0" width="140.350877" height="11.9298746" rx="2"></rect>
      <rect x="17.8947368" y="23.8597491" width="140.350877" height="11.9298746" rx="2"></rect>
      <rect x="166.315789" y="23.8597491" width="173.684211" height="11.9298746" rx="2"></rect>
    </clippath>

    <lineargradient id="animated-diff-gradient" x1="0" x2="0" y1="0" y2="1" spreadMethod="reflect">
      <stop offset="0" stop-color="#eee"></stop>
      <stop offset="0.2" stop-color="#eee"></stop>
      <stop offset="0.5" stop-color="#ddd"></stop>
      <stop offset="0.8" stop-color="#eee"></stop>
      <stop offset="1" stop-color="#eee"></stop>
      <animatetransform attributeName="y1" values="0%; 100%; 0" dur="1s" repeatCount="3"></animatetransform>
      <animatetransform attributeName="y2" values="100%; 200%; 0" dur="1s" repeatCount="3"></animatetransform>
    </lineargradient>
  </defs>
</svg>


            <div id="all_commit_comments" class="js-quote-selection-container" data-quote-markdown=".js-comment-body">
  <div class="mb-1 mb-md-3">
    
<div id="partial-visible-comments-header" class="d-flex flex-items-center flex-column-reverse flex-md-row">
  <h3 class="h4 flex-auto text-md-left text-center">
    0 comments
    on commit <code class="commit-sha">9515ecf</code>
  </h3>

  <div class="flex-shrink-0 mb-2 mb-md-0">
    
  </div>
</div>

  </div>

  <div id="comments" class="comment-holder ml-0 pl-0 ml-md-6 pl-md-3">
    

  <!-- Rendered timeline since 2023-11-25 17:23:15 -->
  <div id="partial-timeline-marker" class="js-timeline-marker js-socket-channel js-updatable-content" data-channel="eyJjIjoicmVwbzo3MTM2NzA2NzI6Y29tbWl0Ojk1MTVlY2ZiNzBlOTlkY2JkOTFkZDU3ZmQ3Y2ZlN2EzMGJlMTRlMTMiLCJ0IjoxNzIwMzIwMzQ2fQ==--67442c706cf77799d58c18826cca90b8d59a5489434c72206bf9763750e8357b" data-url="/mattfelber/CSE-111-programming-with-functions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13/show_partial?partial=commit%2Ftimeline_marker&amp;since=1700961795" data-last-modified="Sun, 26 Nov 2023 01:23:15 GMT">

  </div>

  </div>

  

  
  <div class="js-comment-container ml-0 pl-0 ml-md-6 pl-md-3">
    <div class="d-none d-md-block">
      <span class="timeline-comment-avatar "><a class="d-inline-block" data-hovercard-type="user" data-hovercard-url="/users/emmanuel2011-program/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/emmanuel2011-program"><img class="avatar avatar-user" src="./test chemisrtry_files/172101276(1)" width="40" height="40" alt="@emmanuel2011-program"></a></span>
    </div>

    <!-- '"` --><!-- </textarea></xmp> --><form class="js-new-comment-form js-needs-timeline-marker-header" data-turbo="false" action="https://github.com/mattfelber/CSE-111-programming-with-functions/commit_comment/create" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="27m5_yI3St1aGVuTJNC2DirY8UnxWmC4lFIzrZ_N76xmGmquxUa22jQZfbHOibJuoISa7oZtTznvXqjIGmy8JA">
      <input type="text" name="required_field_bc39" hidden="hidden" class="form-control"><input type="hidden" name="timestamp" value="1720320346087" autocomplete="off" class="form-control"><input type="hidden" name="timestamp_secret" value="2ee2384b175de2d5f1858b9614b6216dbd6bbfef0f835b8045c50e2182fd1fed" autocomplete="off" class="form-control">
      <div>
          <input type="hidden" name="commit_id" value="9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13">
          <input type="hidden" name="path" value="">
            

<label for="new_commit_comment_field" data-view-component="true" class="sr-only position-absolute">Comment</label>
<tab-container class="js-previewable-comment-form write-selected Box CommentBox" data-preview-url="/preview?markdown_unsupported=false&amp;repository=713670672&amp;subject=9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13&amp;subject_type=Commit">
  <input type="hidden" value="nqLEf3Lt1ZmqMRFNuLoNW2MUZ05-yEEt8YPdOjFZoyabyXmoohcdNmGu6PN3OfdW0tLmQbpdz1UTf4nCwK_53w" data-csrf="true" class="js-data-preview-url-csrf">
  <div class="tabnav CommentBox-header width-full">
      <div class="tabnav-tabs" role="tablist" aria-label="Add a comment">
        <button type="button" class="btn-link tabnav-tab write-tab js-write-tab" role="tab" id="write_tab_previewable-comment-form-component-8cc69b8d-bf78-41f1-b33f-4387d68ff4d9" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;WRITE_TAB&quot;,&quot;label&quot;:null}" aria-selected="true" tabindex="0">
          Write
        </button>
        <button type="button" class="btn-link tabnav-tab preview-tab js-preview-tab" role="tab" id="preview_tab_previewable-comment-form-component-8cc69b8d-bf78-41f1-b33f-4387d68ff4d9" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;PREVIEW_TAB&quot;,&quot;label&quot;:null}" aria-selected="false" tabindex="-1">
          Preview
        </button>
      </div>
    <markdown-toolbar role="presentation" for="new_commit_comment_field" data-no-focus="true" data-view-component="true" class="CommentBox-toolbar">
  <action-bar role="toolbar" data-view-component="true" class="ActionBar" data-catalyst="" style="overflow: visible;">
  <div data-target="action-bar.itemContainer" data-view-component="true" class="ActionBar-item-container">
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-19bba14d-f3cb-47b8-b744-8116027cbc9d" data-md-button="header-3" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;HEADING&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-b8509a38-5a70-4fbf-9d7a-19bff3568979" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="0">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heading Button-visual">
    <path d="M3.75 2a.75.75 0 0 1 .75.75V7h7V2.75a.75.75 0 0 1 1.5 0v10.5a.75.75 0 0 1-1.5 0V8.5h-7v4.75a.75.75 0 0 1-1.5 0V2.75A.75.75 0 0 1 3.75 2Z"></path>
</svg>
</button><tool-tip id="tooltip-b8509a38-5a70-4fbf-9d7a-19bff3568979" for="action-bar-19bba14d-f3cb-47b8-b744-8116027cbc9d" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="position-absolute sr-only" aria-hidden="true" role="tooltip" style="--tool-tip-position-top: 8376.109375px; --tool-tip-position-left: 486.6171875px;"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Heading</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-0d34f957-e102-41e4-b9a4-940b371ebff9" data-md-button="bold" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+b" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;BOLD&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-2b28dcc2-b3d6-4468-9d7e-21e29d0e43f7" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bold Button-visual">
    <path d="M4 2h4.5a3.501 3.501 0 0 1 2.852 5.53A3.499 3.499 0 0 1 9.5 14H4a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1Zm1 7v3h4.5a1.5 1.5 0 0 0 0-3Zm3.5-2a1.5 1.5 0 0 0 0-3H5v3Z"></path>
</svg>
</button><tool-tip id="tooltip-2b28dcc2-b3d6-4468-9d7e-21e29d0e43f7" for="action-bar-0d34f957-e102-41e4-b9a4-940b371ebff9" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="position-absolute sr-only" aria-hidden="true" role="tooltip" style="--tool-tip-position-top: 8376.109375px; --tool-tip-position-left: 529.0390625px;"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Bold</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-20d5005b-42a1-4242-926b-e75fd04674f7" data-md-button="italic" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+i" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;ITALIC&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-54c91238-4f99-4830-a2d8-99f792783759" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-italic Button-visual">
    <path d="M6 2.75A.75.75 0 0 1 6.75 2h6.5a.75.75 0 0 1 0 1.5h-2.505l-3.858 9H9.25a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1 0-1.5h2.505l3.858-9H6.75A.75.75 0 0 1 6 2.75Z"></path>
</svg>
</button><tool-tip id="tooltip-54c91238-4f99-4830-a2d8-99f792783759" for="action-bar-20d5005b-42a1-4242-926b-e75fd04674f7" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="position-absolute sr-only" aria-hidden="true" role="tooltip" style="--tool-tip-position-top: 8376.109375px; --tool-tip-position-left: 560.6171875px;"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Italic</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-dff5afd0-a7a5-4013-84ee-4efe1fa783b7" data-md-button="quote" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+Shift+&gt;" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;QUOTE&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-61e05a48-85b6-4662-9dfb-dd8bd4a71ea9" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-quote Button-visual">
    <path d="M1.75 2.5h10.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Zm4 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2.5 7.75v6a.75.75 0 0 1-1.5 0v-6a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</button><tool-tip id="tooltip-61e05a48-85b6-4662-9dfb-dd8bd4a71ea9" for="action-bar-dff5afd0-a7a5-4013-84ee-4efe1fa783b7" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Quote</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-69d01719-b829-410f-81d1-6f70adc8df5c" data-md-button="code" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+e" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;CODE&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-d52599b0-fb22-4985-8865-6dc90311d52e" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code Button-visual">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-d52599b0-fb22-4985-8865-6dc90311d52e" for="action-bar-69d01719-b829-410f-81d1-6f70adc8df5c" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Code</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-ded8ebfc-d6ad-417b-a3c9-d30594473a36" data-md-button="link" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+k" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;LINK&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-90fcfb11-d421-4f2b-ae96-36403518c266" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link Button-visual">
    <path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path>
</svg>
</button><tool-tip id="tooltip-90fcfb11-d421-4f2b-ae96-36403518c266" for="action-bar-ded8ebfc-d6ad-417b-a3c9-d30594473a36" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="position-absolute sr-only" aria-hidden="true" role="tooltip" style="--tool-tip-position-top: 8376.109375px; --tool-tip-position-left: 658.328125px;"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Link</tool-tip>
</div>
      <hr role="presentation" aria-hidden="true" data-targets="action-bar.items" data-view-component="true" class="ActionBar-item ActionBar-divider" data-offset-width="17" style="visibility: visible;">
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-44a73308-2c38-4be7-bdbe-58e6d38392d1" data-md-button="ordered-list" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+Shift+&amp;" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;ORDERED_LIST&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-8f04ec2a-42ec-488d-8a4e-e1385542ff59" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-list-ordered Button-visual">
    <path d="M5 3.25a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 5 3.25Zm0 5a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 5 8.25Zm0 5a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1-.75-.75ZM.924 10.32a.5.5 0 0 1-.851-.525l.001-.001.001-.002.002-.004.007-.011c.097-.144.215-.273.348-.384.228-.19.588-.392 1.068-.392.468 0 .858.181 1.126.484.259.294.377.673.377 1.038 0 .987-.686 1.495-1.156 1.845l-.047.035c-.303.225-.522.4-.654.597h1.357a.5.5 0 0 1 0 1H.5a.5.5 0 0 1-.5-.5c0-1.005.692-1.52 1.167-1.875l.035-.025c.531-.396.8-.625.8-1.078a.57.57 0 0 0-.128-.376C1.806 10.068 1.695 10 1.5 10a.658.658 0 0 0-.429.163.835.835 0 0 0-.144.153ZM2.003 2.5V6h.503a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1h.503V3.308l-.28.14a.5.5 0 0 1-.446-.895l1.003-.5a.5.5 0 0 1 .723.447Z"></path>
</svg>
</button><tool-tip id="tooltip-8f04ec2a-42ec-488d-8a4e-e1385542ff59" for="action-bar-44a73308-2c38-4be7-bdbe-58e6d38392d1" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Numbered list</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-0bf0fca2-9349-4f73-a0d0-120c9d3cb7e2" data-md-button="unordered-list" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+Shift+*" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;UNORDERED_LIST&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-3531cb64-5758-43a1-979f-0615b953f9b3" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-list-unordered Button-visual">
    <path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
</button><tool-tip id="tooltip-3531cb64-5758-43a1-979f-0615b953f9b3" for="action-bar-0bf0fca2-9349-4f73-a0d0-120c9d3cb7e2" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Unordered list</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-dcacc0fa-49b8-4be5-bdd0-318b127246e5" data-md-button="task-list" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+Shift+L" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;TASK_LIST&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-ec1b99ac-5c1d-453f-89b4-2f7008da7898" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tasklist Button-visual">
    <path d="M2 2h4a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1Zm4.655 8.595a.75.75 0 0 1 0 1.06L4.03 14.28a.75.75 0 0 1-1.06 0l-1.5-1.5a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l.97.97 2.095-2.095a.75.75 0 0 1 1.06 0ZM9.75 2.5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm0 5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm0 5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm-7.25-9v3h3v-3Z"></path>
</svg>
</button><tool-tip id="tooltip-ec1b99ac-5c1d-453f-89b4-2f7008da7898" for="action-bar-dcacc0fa-49b8-4be5-bdd0-318b127246e5" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="position-absolute sr-only" aria-hidden="true" role="tooltip" style="--tool-tip-position-top: 8376.109375px; --tool-tip-position-left: 761.8046875px;"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Task list</tool-tip>
</div>
      <hr role="presentation" aria-hidden="true" data-targets="action-bar.items" data-view-component="true" class="ActionBar-item ActionBar-divider" data-offset-width="17" style="visibility: visible;">
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-3872c138-6195-4390-83fc-65ae9d6a694c" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;ATTACH_FILES&quot;,&quot;label&quot;:null}" data-file-attachment-for="fc-new_commit_comment_field" aria-labelledby="tooltip-c9374b54-de98-4052-a46f-016566f29829" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-paperclip Button-visual">
    <path d="M12.212 3.02a1.753 1.753 0 0 0-2.478.003l-5.83 5.83a3.007 3.007 0 0 0-.88 2.127c0 .795.315 1.551.88 2.116.567.567 1.333.89 2.126.89.79 0 1.548-.321 2.116-.89l5.48-5.48a.75.75 0 0 1 1.061 1.06l-5.48 5.48a4.492 4.492 0 0 1-3.177 1.33c-1.2 0-2.345-.487-3.187-1.33a4.483 4.483 0 0 1-1.32-3.177c0-1.195.475-2.341 1.32-3.186l5.83-5.83a3.25 3.25 0 0 1 5.553 2.297c0 .863-.343 1.691-.953 2.301L7.439 12.39c-.375.377-.884.59-1.416.593a1.998 1.998 0 0 1-1.412-.593 1.992 1.992 0 0 1 0-2.828l5.48-5.48a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-5.48 5.48a.492.492 0 0 0 0 .707.499.499 0 0 0 .352.154.51.51 0 0 0 .356-.154l5.833-5.827a1.755 1.755 0 0 0 0-2.481Z"></path>
</svg>
</button><tool-tip id="tooltip-c9374b54-de98-4052-a46f-016566f29829" for="action-bar-3872c138-6195-4390-83fc-65ae9d6a694c" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="position-absolute sr-only" aria-hidden="true" role="tooltip" style="--tool-tip-position-top: 8376.109375px; --tool-tip-position-left: 801.7109375px;"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Attach files</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: hidden;"><button id="action-bar-dca806c5-027c-49b3-814b-342baa2fe982" data-md-button="mention" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;MENTION&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-a4eec0af-d731-41c1-b843-dc6d173f81f5" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-mention Button-visual">
    <path d="M4.75 2.37a6.501 6.501 0 0 0 6.5 11.26.75.75 0 0 1 .75 1.298A7.999 7.999 0 0 1 .989 4.148 8 8 0 0 1 16 7.75v1.5a2.75 2.75 0 0 1-5.072 1.475 3.999 3.999 0 0 1-6.65-4.19A4 4 0 0 1 12 8v1.25a1.25 1.25 0 0 0 2.5 0V7.867a6.5 6.5 0 0 0-9.75-5.496ZM10.5 8a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>
</button><tool-tip id="tooltip-a4eec0af-d731-41c1-b843-dc6d173f81f5" for="action-bar-dca806c5-027c-49b3-814b-342baa2fe982" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Mention</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: hidden;"><button id="action-bar-80a2c1b2-c5dc-4cee-bd4d-8a5bc4ffdbc7" data-md-button="ref" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;REFERENCE&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-73fe9f5b-01f6-4e37-8193-cdb978ad6a70" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-cross-reference Button-visual">
    <path d="M2.75 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h4.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 13H9.06l-2.573 2.573A1.458 1.458 0 0 1 4 14.543V13H2.75A1.75 1.75 0 0 1 1 11.25v-7.5C1 2.784 1.784 2 2.75 2h5.5a.75.75 0 0 1 0 1.5ZM16 1.25v4.146a.25.25 0 0 1-.427.177L14.03 4.03l-3.75 3.75a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l3.75-3.75-1.543-1.543A.25.25 0 0 1 11.604 1h4.146a.25.25 0 0 1 .25.25Z"></path>
</svg>
</button><tool-tip id="tooltip-73fe9f5b-01f6-4e37-8193-cdb978ad6a70" for="action-bar-80a2c1b2-c5dc-4cee-bd4d-8a5bc4ffdbc7" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Reference</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: hidden;"><button id="action-bar-c6e362b8-f110-4b98-9541-3f12a75f4b40" data-show-dialog-id="saved_replies_menu_new_commit_comment_field-dialog" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;SAVED_REPLIES&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-19bc729c-afcb-47c4-8b30-0b0b539dab61" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-reply Button-visual">
    <path d="M6.78 1.97a.75.75 0 0 1 0 1.06L3.81 6h6.44A4.75 4.75 0 0 1 15 10.75v2.5a.75.75 0 0 1-1.5 0v-2.5a3.25 3.25 0 0 0-3.25-3.25H3.81l2.97 2.97a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L1.47 7.28a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</button><tool-tip id="tooltip-19bc729c-afcb-47c4-8b30-0b0b539dab61" for="action-bar-c6e362b8-f110-4b98-9541-3f12a75f4b40" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Saved replies</tool-tip>
</div>
</div>    <action-menu data-target="action-bar.moreMenu" data-select-variant="none" data-view-component="true" class="ActionBar-more-menu" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-bar-ffbd1dd3-a536-4407-abbb-f6e1959bacd9-button" popovertarget="action-bar-ffbd1dd3-a536-4407-abbb-f6e1959bacd9-overlay" aria-controls="action-bar-ffbd1dd3-a536-4407-abbb-f6e1959bacd9-list" aria-haspopup="true" aria-labelledby="tooltip-f93bc94e-39b7-4422-8d36-832097f9a4b8" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-f93bc94e-39b7-4422-8d36-832097f9a4b8" for="action-bar-ffbd1dd3-a536-4407-abbb-f6e1959bacd9-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--fgColor-onEmphasis, var(--color-fg-on-emphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--bgColor-emphasis, var(--color-neutral-emphasis-plus)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Menu</tool-tip>


<anchored-position id="action-bar-ffbd1dd3-a536-4407-abbb-f6e1959bacd9-overlay" anchor="action-bar-ffbd1dd3-a536-4407-abbb-f6e1959bacd9-button" align="end" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 0px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-bar-ffbd1dd3-a536-4407-abbb-f6e1959bacd9-button" id="action-bar-ffbd1dd3-a536-4407-abbb-f6e1959bacd9-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li value="" hidden="" data-for="action-bar-19bba14d-f3cb-47b8-b744-8116027cbc9d" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-0c9c4db6-562f-49d2-aa6d-54de5745e64c" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heading">
    <path d="M3.75 2a.75.75 0 0 1 .75.75V7h7V2.75a.75.75 0 0 1 1.5 0v10.5a.75.75 0 0 1-1.5 0V8.5h-7v4.75a.75.75 0 0 1-1.5 0V2.75A.75.75 0 0 1 3.75 2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Heading
</span></button>
  
</li>
        <li value="" hidden="" data-for="action-bar-0d34f957-e102-41e4-b9a4-940b371ebff9" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-c801db67-9f13-471d-8adb-9c299f6905e9" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bold">
    <path d="M4 2h4.5a3.501 3.501 0 0 1 2.852 5.53A3.499 3.499 0 0 1 9.5 14H4a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1Zm1 7v3h4.5a1.5 1.5 0 0 0 0-3Zm3.5-2a1.5 1.5 0 0 0 0-3H5v3Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Bold
</span></button>
  
</li>
        <li value="" hidden="" data-for="action-bar-20d5005b-42a1-4242-926b-e75fd04674f7" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-d1a41191-98ce-43f7-9944-6f5bd5834b68" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-italic">
    <path d="M6 2.75A.75.75 0 0 1 6.75 2h6.5a.75.75 0 0 1 0 1.5h-2.505l-3.858 9H9.25a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1 0-1.5h2.505l3.858-9H6.75A.75.75 0 0 1 6 2.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Italic
</span></button>
  
</li>
        <li value="" hidden="" data-for="action-bar-dff5afd0-a7a5-4013-84ee-4efe1fa783b7" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-3af6cf31-b4d5-4889-b6b1-bd5380fabbc9" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-quote">
    <path d="M1.75 2.5h10.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Zm4 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2.5 7.75v6a.75.75 0 0 1-1.5 0v-6a.75.75 0 0 1 1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Quote
</span></button>
  
</li>
        <li value="" hidden="" data-for="action-bar-69d01719-b829-410f-81d1-6f70adc8df5c" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-71e744b1-85cb-4923-aeea-8c85d06a1188" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span></button>
  
</li>
        <li value="" hidden="" data-for="action-bar-ded8ebfc-d6ad-417b-a3c9-d30594473a36" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-48f5dc8c-a447-4c56-a2f6-416635a9b29c" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link">
    <path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Link
</span></button>
  
</li>
        <li hidden="" role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        <li value="" hidden="" data-for="action-bar-44a73308-2c38-4be7-bdbe-58e6d38392d1" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-eaf70b69-4105-4b5b-a9cc-3b85824b8012" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-list-ordered">
    <path d="M5 3.25a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 5 3.25Zm0 5a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 5 8.25Zm0 5a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1-.75-.75ZM.924 10.32a.5.5 0 0 1-.851-.525l.001-.001.001-.002.002-.004.007-.011c.097-.144.215-.273.348-.384.228-.19.588-.392 1.068-.392.468 0 .858.181 1.126.484.259.294.377.673.377 1.038 0 .987-.686 1.495-1.156 1.845l-.047.035c-.303.225-.522.4-.654.597h1.357a.5.5 0 0 1 0 1H.5a.5.5 0 0 1-.5-.5c0-1.005.692-1.52 1.167-1.875l.035-.025c.531-.396.8-.625.8-1.078a.57.57 0 0 0-.128-.376C1.806 10.068 1.695 10 1.5 10a.658.658 0 0 0-.429.163.835.835 0 0 0-.144.153ZM2.003 2.5V6h.503a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1h.503V3.308l-.28.14a.5.5 0 0 1-.446-.895l1.003-.5a.5.5 0 0 1 .723.447Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Numbered list
</span></button>
  
</li>
        <li value="" hidden="" data-for="action-bar-0bf0fca2-9349-4f73-a0d0-120c9d3cb7e2" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-2d655787-4a6b-417b-855b-76df8d43cb53" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-list-unordered">
    <path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Unordered list
</span></button>
  
</li>
        <li value="" hidden="" data-for="action-bar-dcacc0fa-49b8-4be5-bdd0-318b127246e5" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-8cb63e2a-5ab0-42b8-a9b7-9d455f9cc5d0" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tasklist">
    <path d="M2 2h4a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1Zm4.655 8.595a.75.75 0 0 1 0 1.06L4.03 14.28a.75.75 0 0 1-1.06 0l-1.5-1.5a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l.97.97 2.095-2.095a.75.75 0 0 1 1.06 0ZM9.75 2.5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm0 5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm0 5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm-7.25-9v3h3v-3Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Task list
</span></button>
  
</li>
        <li hidden="" role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        <li value="" hidden="" data-for="action-bar-3872c138-6195-4390-83fc-65ae9d6a694c" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-0bc9a3d3-29d4-47ee-81c8-fd86459c1d39" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-paperclip">
    <path d="M12.212 3.02a1.753 1.753 0 0 0-2.478.003l-5.83 5.83a3.007 3.007 0 0 0-.88 2.127c0 .795.315 1.551.88 2.116.567.567 1.333.89 2.126.89.79 0 1.548-.321 2.116-.89l5.48-5.48a.75.75 0 0 1 1.061 1.06l-5.48 5.48a4.492 4.492 0 0 1-3.177 1.33c-1.2 0-2.345-.487-3.187-1.33a4.483 4.483 0 0 1-1.32-3.177c0-1.195.475-2.341 1.32-3.186l5.83-5.83a3.25 3.25 0 0 1 5.553 2.297c0 .863-.343 1.691-.953 2.301L7.439 12.39c-.375.377-.884.59-1.416.593a1.998 1.998 0 0 1-1.412-.593 1.992 1.992 0 0 1 0-2.828l5.48-5.48a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-5.48 5.48a.492.492 0 0 0 0 .707.499.499 0 0 0 .352.154.51.51 0 0 0 .356-.154l5.833-5.827a1.755 1.755 0 0 0 0-2.481Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Attach files
</span></button>
  
</li>
        <li value="" data-for="action-bar-dca806c5-027c-49b3-814b-342baa2fe982" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-b904b3a6-589a-4020-b9d9-a71bf8f94f5a" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-mention">
    <path d="M4.75 2.37a6.501 6.501 0 0 0 6.5 11.26.75.75 0 0 1 .75 1.298A7.999 7.999 0 0 1 .989 4.148 8 8 0 0 1 16 7.75v1.5a2.75 2.75 0 0 1-5.072 1.475 3.999 3.999 0 0 1-6.65-4.19A4 4 0 0 1 12 8v1.25a1.25 1.25 0 0 0 2.5 0V7.867a6.5 6.5 0 0 0-9.75-5.496ZM10.5 8a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Mention
</span></button>
  
</li>
        <li value="" data-for="action-bar-80a2c1b2-c5dc-4cee-bd4d-8a5bc4ffdbc7" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-122324ed-08fd-4188-998c-a9840594acf1" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-cross-reference">
    <path d="M2.75 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h4.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 13H9.06l-2.573 2.573A1.458 1.458 0 0 1 4 14.543V13H2.75A1.75 1.75 0 0 1 1 11.25v-7.5C1 2.784 1.784 2 2.75 2h5.5a.75.75 0 0 1 0 1.5ZM16 1.25v4.146a.25.25 0 0 1-.427.177L14.03 4.03l-3.75 3.75a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l3.75-3.75-1.543-1.543A.25.25 0 0 1 11.604 1h4.146a.25.25 0 0 1 .25.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Reference
</span></button>
  
</li>
        <li value="" data-for="action-bar-c6e362b8-f110-4b98-9541-3f12a75f4b40" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-bad37558-92d5-4944-b93d-1805299b6afc" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-reply">
    <path d="M6.78 1.97a.75.75 0 0 1 0 1.06L3.81 6h6.44A4.75 4.75 0 0 1 15 10.75v2.5a.75.75 0 0 1-1.5 0v-2.5a3.25 3.25 0 0 0-3.25-3.25H3.81l2.97 2.97a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L1.47 7.28a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Saved replies
</span></button>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></action-bar></markdown-toolbar>

<dialog-helper>
  <dialog id="saved_replies_menu_new_commit_comment_field-dialog" aria-modal="true" aria-labelledby="saved_replies_menu_new_commit_comment_field-dialog-title" aria-describedby="saved_replies_menu_new_commit_comment_field-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--placement-bottom-whenNarrow js-saved-reply-container">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="saved_replies_menu_new_commit_comment_field-dialog-title">
        Select a reply
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="saved_replies_menu_new_commit_comment_field-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="saved_replies_menu_new_commit_comment_field-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">    <include-fragment class="js-saved-reply-include-fragment" role="menuitem" aria-label="Loading" src="/settings/replies?context=none" loading="lazy"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="my-6 mx-auto d-block anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>  <span class="sr-only">Loading</span>

    </include-fragment>
</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">    <a href="https://github.com/settings/replies?return_to=1" data-view-component="true" class="Button--invisible Button--medium Button Button--fullWidth">  <span class="Button-content Button-content--alignStart">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label">Create a new saved reply</span>
  </span>
</a>
</div>
</dialog></dialog-helper>


  </div>

  <div class="comment-form-error js-comment-form-error" role="alert" hidden="">
    There was an error creating your Commit.
  </div>

  <file-attachment class="js-upload-markdown-image is-default" input="fc-new_commit_comment_field" role="tabpanel" aria-labelledby="write_tab_previewable-comment-form-component-8cc69b8d-bf78-41f1-b33f-4387d68ff4d9" data-tab-container-no-tabstop="true" data-upload-repository-id="713670672" data-upload-policy-url="/upload/policies/assets"><input type="hidden" value="O-xeFI6kf2vA68IVfX_ZlizROknD8vwYNnXLWv0lnh62QoWuOO3121EVa_15Yvad0-84HPPai-yVgMYneszEUQ" data-csrf="true" class="js-data-upload-policy-url-csrf">
    <div class="js-write-bucket position-relative">
        <input type="hidden" name="saved_reply_id" id="new_commit_comment_field_saved_reply_id" class="js-resettable-field" value="" data-reset-value="">

      <text-expander keys=": @ #" data-issue-url="/suggestions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13?issue_suggester=1&amp;repository=CSE-111-programming-with-functions&amp;user_id=mattfelber" data-mention-url="/suggestions/commit/9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13?mention_suggester=1&amp;repository=CSE-111-programming-with-functions&amp;user_id=mattfelber" multiword="#" data-emoji-url="/autocomplete/emoji">
          
        <div class="CommentBox-container">
          <textarea name="comment[body]" id="new_commit_comment_field" placeholder=" " data-required-trimmed="Text field is empty" class="js-comment-field js-paste-markdown js-task-list-field js-quick-submit FormControl-textarea CommentBox-input js-size-to-fit js-session-resumable js-saved-reply-shortcut-comment-field" dir="auto" aria-describedby="placeholder_previewable-comment-form-component-8cc69b8d-bf78-41f1-b33f-4387d68ff4d9" required=""></textarea>
          <p class="CommentBox-placeholder" id="placeholder_previewable-comment-form-component-8cc69b8d-bf78-41f1-b33f-4387d68ff4d9" data-comment-box-placeholder="" aria-hidden="true">
            Leave a comment
          </p>
        </div>

      </text-expander>
        <input accept=".gif,.jpeg,.jpg,.mov,.mp4,.png,.svg,.webm,.cpuprofile,.csv,.dmp,.docx,.fodg,.fodp,.fods,.fodt,.gz,.json,.jsonc,.log,.md,.odf,.odg,.odp,.ods,.odt,.patch,.pdf,.pptx,.tgz,.txt,.xls,.xlsx,.zip" type="file" multiple="" hidden="" id="fc-new_commit_comment_field">
        <div class="file-attachment-errors">
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 bad-file repository-required Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">We don’t support that file type.</p>
        <p>Try again with GIF, JPEG, JPG, MOV, MP4, PNG, SVG, WEBM, CPUPROFILE, CSV, DMP, DOCX, FODG, FODP, FODS, FODT, GZ, JSON, JSONC, LOG, MD, ODF, ODG, ODP, ODS, ODT, PATCH, PDF, PPTX, TGZ, TXT, XLS, XLSX or ZIP.</p>
</div></div></x-banner>
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 bad-permissions Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">Attaching documents requires write permission to this repository.</p>
        <p>Try again with GIF, JPEG, JPG, MOV, MP4, PNG, SVG, WEBM, CPUPROFILE, CSV, DMP, DOCX, FODG, FODP, FODS, FODT, GZ, JSON, JSONC, LOG, MD, ODF, ODG, ODP, ODS, ODT, PATCH, PDF, PPTX, TGZ, TXT, XLS, XLSX or ZIP.</p>
</div></div></x-banner>
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 too-big js-upload-too-big Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText"></p>
</div></div></x-banner>
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 empty Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">This file is empty.</p>
        <p>Try again with a file that’s not empty.</p>
</div></div></x-banner>
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 hidden-file Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">This file is hidden.</p>
        <p>Try again with another file.</p>
</div></div></x-banner>
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 failed-request Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">Something went really wrong, and we can’t process that file.</p>
        <p>Try again.</p>
</div></div></x-banner>
        </div>
    </div>

    <div class="pr-2 pl-2 pb-2">
      <div data-view-component="true" class="border-right color-border-muted d-inline-block mr-1 pr-2">
        <a href="https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax" target="_blank" rel="noopener noreferrer" data-ga-click="Markdown Toolbar, click, help" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;MARKDOWN_BUTTON&quot;,&quot;label&quot;:null}" data-view-component="true" class="Button--invisible Button--small Button">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-markdown">
    <path d="M14.85 3c.63 0 1.15.52 1.14 1.15v7.7c0 .63-.51 1.15-1.15 1.15H1.15C.52 13 0 12.48 0 11.84V4.15C0 3.52.52 3 1.15 3ZM9 11V5H7L5.5 7 4 5H2v6h2V8l1.5 1.92L7 8v3Zm2.99.5L14.5 8H13V5h-2v3H9.5Z"></path>
</svg>
      </span>
    <span class="Button-label">Markdown is supported</span>
  </span>
</a>
</div>        <button data-file-attachment-for="fc-new_commit_comment_field" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;UPLOAD_BUTTON&quot;,&quot;label&quot;:null}" type="button" data-view-component="true" class="Button--invisible Button--small Button">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-image">
    <path d="M16 13.25A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75C0 1.784.784 1 1.75 1h12.5c.966 0 1.75.784 1.75 1.75ZM1.75 2.5a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h.94l.03-.03 6.077-6.078a1.75 1.75 0 0 1 2.412-.06L14.5 10.31V2.75a.25.25 0 0 0-.25-.25Zm12.5 11a.25.25 0 0 0 .25-.25v-.917l-4.298-3.889a.25.25 0 0 0-.344.009L4.81 13.5ZM7 6a2 2 0 1 1-3.999.001A2 2 0 0 1 7 6ZM5.5 6a.5.5 0 1 0-1 0 .5.5 0 0 0 1 0Z"></path>
</svg>
      </span>
    <span class="Button-label">Paste, drop, or click to add files</span>
  </span>
</button>
    </div>
</file-attachment>
  <div role="tabpanel" class="js-preview-panel overflow-auto CommentBox-comment" aria-labelledby="preview_tab_previewable-comment-form-component-8cc69b8d-bf78-41f1-b33f-4387d68ff4d9" hidden="">
    <input type="hidden" name="path" value="" class="js-path">
    <input type="hidden" name="line" value="" class="js-line-number">
    <input type="hidden" name="start_line" value="" class="js-start-line-number">
    <input type="hidden" name="preview_side" value="" class="js-side">
    <input type="hidden" name="preview_start_side" value="" class="js-start-side">
    <input type="hidden" name="start_commit_oid" value="" class="js-start-commit-oid">
    <input type="hidden" name="end_commit_oid" value="" class="js-end-commit-oid">
    <input type="hidden" name="base_commit_oid" value="" class="js-base-commit-oid">
    <input type="hidden" name="comment_id" value="" class="js-comment-id">
    <div class="comment js-suggested-changes-container" data-thread-side="">
  <div class="comment-body markdown-body js-preview-body">
    <p>Nothing to preview</p>
  </div>
</div>

  </div>

  <div class="comment-form-error mb-2 js-comment-update-error" hidden=""></div>
</tab-container>


            <div class="d-flex flex-items-center flex-justify-end gap-2 my-2">
              <button data-disable-invalid="" data-disable-with="" type="submit" data-view-component="true" class="Button--primary Button--medium Button" disabled="">  <span class="Button-content">
    <span class="Button-label">Comment on this commit</span>
  </span>
</button>

            </div>
      </div>
</form>
  </div>

</div>

                <div class="thread-subscription-status js-socket-channel js-updatable-content" data-replace-remote-form-target="" data-channel="eyJjIjoibGlzdC1zdWJzY3JpcHRpb246cmVwb3NpdG9yeTo3MTM2NzA2NzI6MTcyMTAxMjc2IiwidCI6MTcyMDMyMDQ3MX0=--a62f4269baa994c396414596e43135ef0eb9a32412c04d5e710a3d76d2d6b76a eyJjIjoidGhyZWFkLXN1YnNjcmlwdGlvbjo5NTE1ZWNmYjcwZTk5ZGNiZDkxZGQ1N2ZkN2NmZTdhMzBiZTE0ZTEzOjE3MjEwMTI3NiIsInQiOjE3MjAzMjA0NzF9--9866d91c835a60dd24c1f8b994a1baad801d6f6968036ed85c20218b86dfa361" data-url="/notifications/thread_subscription?repository_id=713670672&amp;thread_class=Commit&amp;thread_id=9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13">
      <!-- '"` --><!-- </textarea></xmp> --><form data-replace-remote-form="true" class="thread-subscribe-form" data-turbo="false" action="https://github.com/notifications/thread" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="QrLm3lZWuNYucVSwqBNIJ2xe2_y2U0UsCODWBQEiZW7d2eve9qqJvBAsBR9G-qqo_kdvlktiXUOQ2exx1HKWzA" autocomplete="off">        <input type="hidden" name="repository_id" value="713670672">
        <input type="hidden" name="thread_id" value="9515ecfb70e99dcbd91dd57fd7cfe7a30be14e13">
        <input type="hidden" name="thread_class" value="Commit">
        <input type="hidden" name="id" value="subscribe">
        <button data-thread-subscribe-button="" data-disable-with="" aria-describedby="notification-subscribe-button-reason" type="submit" data-view-component="true" class="Button--secondary Button--small Button Button--fullWidth">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell">
    <path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path>
</svg>
      </span>
    <span class="Button-label">Subscribe</span>
  </span>
</button>
</form>      <p id="notification-subscribe-button-reason" class="reason text-small color-fg-muted" aria-live="polite">
        You’re not receiving notifications from this thread.
      </p>
  </div>

</div>
</div>  </diff-layout>


</div>


  </div>

</turbo-frame>


    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 16 16" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
</svg>
</a>
      <span>
        © 2024 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mr-3">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement">
      Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mr-3">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>




    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>


  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/emmanuel2011-program"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
        padding: 0 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true">chemistry · mattfelber/CSE-111-programming-with-functions@9515ecf</div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


<div class="sr-only mt-n1" id="screenReaderAnnouncementDiv" role="alert" data-testid="screenReaderAnnouncement" aria-live="assertive"></div><div id="__primerPortalRoot__" style="position: absolute; top: 0px; left: 0px;"></div></body></html>